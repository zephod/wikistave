import requests
import re
import sys
import time

SERVER_URL = 'http://code/wikistave/scrape'
SERVER_URL = 'http://www.ultimate-guitar.com'

### 
### Utilities 
### 
def download(url):
    time.sleep(0.2)
    if url[0]=='/': 
        url = SERVER_URL + url
    else:
        url = SERVER_URL + '/' + url
    print "GET",url
    r = requests.get(url)
    if not r.status_code==200:
        raise ValueError('[requests]: GET %s\n[requests]: code=%s' % (url, str(r.status_code)))
    return r.content

def get_regex(regex,doc,expected=True):
    matches = re.search(regex,doc)
    if not matches:
        if expected: 
            raise ValueError('Regex does not match: %s' % regex)
        return None
    return matches.group(1)


### 
### Scrapers
### 
def ug_song_urls_from_letter(letter_start_url):
    regex  = 'href="(/tabs/[^"]+)"'
    regex2 = '<a [^>]*href="([^"]*)"[^>]*>Next'
    session = db.connect()
    next_url = letter_start_url
    while (next_url): 
        doc = download(next_url)
        # Go through each artist in turn
        for match in re.finditer(regex,doc):
            ug_song_urls_from_artist(match.group(1),session)
        next_url = get_regex(regex2,doc,expected=False)

def ug_song_urls_from_artist(artist_start_url,session=None):
    if not session: session = db.connect()
    regex = '<a .*href="([^"]*)".*guitar pro tabs only'
    regex2 = '<title>(.*)Tabs.*:'
    regex3 = '<a [^>]*href="([^"]*)"[^>]*>Next'
    regex4 = 'href="([^"]*ultimate-guitar.com/[a-z]/[^"]*)"'
    try:
        doc = download(artist_start_url)
        # Does this artist have a guitar pro tab page?
        next_url = get_regex(regex,doc,expected=False)
        if not next_url:
            print 'Artist does not have Guitar Pro tabs.'
            return
        # What's the artist's name?
        _artist_name = get_regex(regex2,doc).strip()
        artist_id = db.create_artist_id(session,_artist_name)
        if artist_id < 0: 
            print "Already scraped this artist."
            return
        # Look for the link to the next page
        while (next_url): 
            doc = download(next_url)
            # Pull all the song links off this doc
            n = 0
            for match in re.finditer(regex4,doc):
                n += 1
                st = db.SongTarget(artist_id, match.group(1))
                session.add(st)
            print "    ...got %d urls" % n
            next_url = get_regex(regex3,doc,expected=False)
        print "[committing...]"
        session.commit()
        print "[...done]"
    except Exception as err:
        print >>sys.stderr, ("== EXCEPTION == (start_url=%s)"%artist_start_url)
        print >>sys.stderr, err


__all__ = ['ug_song_urls_from_artist', 'ug_song_urls_from_letter']

