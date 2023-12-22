
#from changedetectionio import queuedWatchMetaData
from copy import deepcopy
from distutils.util import strtobool
from feedgen.feed import FeedGenerator
from flask_compress import Compress as FlaskCompress
from flask_login import current_user
from flask_restful import abort, Api
from flask_wtf import CSRFProtect
from functools import wraps
from threading import Event
import datetime
import flask_login
import logging
import os
import pytz
import queue
import threading
import time
import timeago

from flask import (
    Flask,
    abort,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)

from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__,
            static_url_path="",
            static_folder="static",
            template_folder="templates")

FlaskCompress(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/static")
def static_content():
    # https://github.com/dgtlmoon/changedetection.io/blob/3d1e1025d2eea3085c6247d6b88905ffe7b84a40/changedetectionio/flask_app.py#L1239C1-L1239C81
    return send_from_directory("static", path="image.png")
