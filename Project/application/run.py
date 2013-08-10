#!flask/bin/python
from os import environ

environ['CONFIGURATION'] = '/project/application/configuration.py'

from morgan import app

app.run('0.0.0.0', 80)
