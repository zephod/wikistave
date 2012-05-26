from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

OrmObject = declarative_base()

class Artist(OrmObject): 
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Artist.%s'%(self.name)

class SongTarget(OrmObject): 
    __tablename__ = 'song_target'
    artist_id = Column(Integer, primary_key=True)
    song_url = Column(String(256), primary_key=True)

    def __init__(self,artist_id,song_url):
        self.artist_id=artist_id
        self.song_url=song_url

    def __repr__(self):
        return 'SongTarget.%s.(%s)'%(self.artist_id,self.song_url)


class Test(OrmObject): 
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    text = Column(String(256),unique=True)

    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return 'Test\t%s\t"%s"'%(self.id,self.text)


def connect():
    DB_URL  = 'scrape.c0wihxrdkrzz.eu-west-1.rds.amazonaws.com'
    DB_USER = 'scraper'
    DB_PASS = 'wikistave'
    DB_NAME = 'mydb'
    DB_STRING = 'mysql+mysqldb://%s:%s@%s/%s' % (DB_USER,DB_PASS,DB_URL,DB_NAME)

    print 'Connecting:',DB_STRING
    engine = create_engine(DB_STRING)
    OrmObject.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()

def create_artist_id(session,name):
    a = session.query(Artist).filter(Artist.name==name).first()
    if not a:
        a = Artist(name)
        session.add(a)
        session.commit()
        return a.id
    # Signal that this artist has already been created
    return -1


## --
## Entry points
## --
def db_put_test(text): 
    """Write a string into the test table"""
    session = connect()
    t = session.query(Test).filter(Test.text==text).first()
    if not t:
        t = Test(text)
        session.add(t)
        session.commit()
    print t

def db_dump_test(): 
    """Read the test table"""
    session = connect()
    from pprint import pprint
    pprint( session.query(Test).all() )

__all__=['db_dump_test', 'db_put_test']
