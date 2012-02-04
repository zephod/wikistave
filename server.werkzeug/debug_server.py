#!/usr/bin/env python

from werkzeug.serving import run_simple
import app

if __name__=='__main__':
    app = app.create_app()
    run_simple('localhost', 5000, app, use_debugger=True, use_reloader=True)
