from flask import Flask, Response, request
from flask_cors import CORS
from sse import get_user_alarm_by_lang, client_connections
from uuid import uuid4
from threading import Lock


app = Flask(__name__)
CORS(app)


connections_lock = Lock()


@app.get("/connection/<user_id>")
def connection(user_id: str):
    current_conn_id = uuid4().hex

    with connections_lock:
        client_connections[user_id] = current_conn_id

    lang = request.accept_languages.best

    return Response(
        get_user_alarm_by_lang(user_id, lang, current_conn_id),
        content_type="text/event-stream",
    )


if __name__ == "__main__":
    app.run(port=5000)
