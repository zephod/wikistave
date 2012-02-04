from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'We are, each and every one of us, friends at last.'

if __name__ == '__main__':
    app.run()
