from flask import Flask,app
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello this is priyanka ....."

if __name__ == "__main__":
    print("Starting Python Flask server....")
    app.run()