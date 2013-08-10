# -*- coding: utf-8 -*-

"""app.

Write some more shit here. Because no one can make up their mind exactly how to
do this. I really just like the pretty color that shows up in my text editor.

Longer description including the modules and subpackages exported by this
package should go here.

:copyright: Copyright 2013 by Megan Speir

"""

__version__ = "0.0.0"
# $Source$

from flask import Flask, render_template, redirect, abort, request, url_for
from morgan.database import db_session

# from modules.flatpages import FlatPages
# from modules.utilities import Pagination

app = Flask('morgan', static_folder='../../resources', template_folder='../../templates')
app.config.from_object('defaults')
#app.config.from_envvar('CONFIGURATION')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

import morgan.views
