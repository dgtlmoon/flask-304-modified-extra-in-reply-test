#!/usr/bin/python3

import eventlet
import eventlet.wsgi
import socket

from flask import (
    Flask,
    send_from_directory,
)


app = Flask(__name__)


@app.route("/static")
def static_content():
    # https://github.com/dgtlmoon/changedetection.io/blob/3d1e1025d2eea3085c6247d6b88905ffe7b84a40/changedetectionio/flask_app.py#L1239C1-L1239C81
    return send_from_directory("static", path="image.png")

def main():
    s_type = socket.AF_INET
    # This will result in 'Excess found' extra content in 304 modified which is against the RFC
    eventlet.wsgi.server(eventlet.listen(("127.0.0.1", int(5000)), s_type), app)

if __name__ == '__main__':
    main()

