import os

_basedir = os.path.abspath(os.path.dirname(__file__))


# Enable/disable debug mode
#DEBUG = False
# Enable/disable testing mode
#TESTING = False
# Explicitly enable or disable the propagation of exceptions. If not set or
# explicitly set to None this is implicitly true if either TESTING or DEBUG is
# true.
#PROPAGATE_EXCEPTIONS
# By default if the application is in debug mode the request context is not
# popped on exceptions to enable debuggers to introspect the data. This can be
# disabled by this key. You can also use this setting to force-enable it for
# non debug execution which might be useful to debug production applications
# (but also very risky).
#PRESERVE_CONTEXT_ON_EXCEPTION
# The secret key
#SECRET_KEY
# The name of the session cookie
#SESSION_COOKIE_NAME
# The domain for the session cookie. If this is not set, the cookie will be
# valid for all subdomains of SERVER_NAME.
#SESSION_COOKIE_DOMAIN
# The path for the session cookie. If this is not set the cookie will be valid
# for all of APPLICATION_ROOT or if that is not set for '/'.
#SESSION_COOKIE_PATH
# Controls if the cookie should be set with the httponly flag. Defaults to True.
#SESSION_COOKIE_HTTPONLY
# Controls if the cookie should be set with the secure flag. Defaults to False.
#SESSION_COOKIE_SECURE
# The lifetime of a permanent session as datetime.timedelta object. Starting
# with Flask 0.8 this can also be an integer representing seconds.
#PERMANENT_SESSION_LIFETIME
# Enable/disable x-sendfile
#USE_X_SENDFILE
# The name of the logger
#LOGGER_NAME
# The name and port number of the server. Required for subdomain support (e.g.:
# 'myapp.dev:5000') Note that localhost does not support subdomains so setting
# this to "localhost" does not help. Setting a SERVER_NAME also by default
# enables URL generation without a request context but with an application context.
#SERVER_NAME
# If the application does not occupy a whole domain or subdomain this can be
# set to the path where the application is configured to live. This is for
# session cookie as path value. If domains are used, this should be None.
#APPLICATION_ROOT
# If set to a value in bytes, Flask will reject incoming requests with a
# content length greater than this by returning a 413 status code.
#MAX_CONTENT_LENGTH
# Default cache control max age to use with send_static_file() (the default
# static file handler) and send_file(), in seconds. Override this value on a
# per-file basis using the get_send_file_max_age() hook on Flask or Blueprint,
# respectively. Defaults to 43200 (12 hours).
#SEND_FILE_MAX_AGE_DEFAULT:
# If this is set to True Flask will not execute the error handlers of HTTP
# exceptions but instead treat the exception like any other and bubble it
# through the exception stack. This is helpful for hairy debugging situations
# where you have to find out where an HTTP exception is coming from.
#TRAP_HTTP_EXCEPTIONS
# Werkzeug's internal data structures that deal with request specific data will
# raise special key errors that are also bad request exceptions. Likewise many
# operations can implicitly fail with a BadRequest exception for consistency.
# Since it's nice for debugging to know why exactly it failed this flag can be
# used to debug those situations. If this config is set to True you will get a
# regular traceback instead.
#TRAP_BAD_REQUEST_ERRORS
# The URL scheme that should be used for URL generation if no URL scheme is
# available. This defaults to http.
#PREFERRED_URL_SCHEME

del os
