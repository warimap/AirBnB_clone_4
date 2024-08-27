#!/usr/bin/python3
"""
imports Flask instance for gunicorn configurations
gunicorn --bind 34.204.60.71:8001 wsgi:web_flask.app
"""

web_flask = __import__('web_flask.6-number_odd_or_even',
                       globals(), locals(), ['*'])

if __name__ == "__main__":
    """runs the main flask app"""
    web_flask.app.run()
