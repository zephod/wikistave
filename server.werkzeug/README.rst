================
WikiStave:Server
================

Lightweight server for WikiStave. Written in Python; uses Werkzeug library.


Install
======= 

This is a Python application with a couple of requirements.

First ensure you've got pip installed.

First, fire up a virtual environment::

  virtualenv %env.stave
  . %env.stave/bin/activate

Install the requirements::

  pip install jinja2 redis werkzeug

Start the server::

  ./debug_server.py

