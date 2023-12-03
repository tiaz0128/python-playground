from flask import Flask, Response, stream_with_context
import time


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask with CORS!"


def generate():
    # This function generates data to be sent to the client
    while True:
        yield f"data: Server time is {time.ctime()}\n\n"
        time.sleep(1)  # Delay to simulate data generation process


@app.route("/stream")
def stream():
    return Response(stream_with_context(generate()), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
