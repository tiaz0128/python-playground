from flask import Flask, Response, Request
from time import sleep
import json

app = Flask(__name__)


def generator(user_id):
    yield f"data: Hello! {user_id}\n\n"

    while True:
        data = {"name": user_id}
        yield f"""event: notice\ndata: {json.dumps(data)}\n\n"""
        sleep(5)


@app.get("/connection/<user_id>")
def connection(user_id: str):
    return Response(generator(user_id), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(port=5000)
