from flask import Flask
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    pass
    # return render_template('404.html'), 404

@app.teardown_request
def shutdown_session(exception=None):
    pass
    # db_session.remove()

@app.route("/")
def hello():
    return "Hello World!"

#if __name__ == "__main__":
#    app.run()
