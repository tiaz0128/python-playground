from time import sleep
import json


client_connections = {}


def select_alarm_by_lang(user_id, lang):
    ...

    return {"message": "예약에 성공했습니다!"}


def get_user_alarm_by_lang(user_id, lang, current_conn_id):
    PENDING_TIME = 5

    while True:
        if client_connections.get(user_id) != current_conn_id:
            print(f"BYE BYE {current_conn_id}")
            break

        data = select_alarm_by_lang(user_id, lang)
        yield f"""event: alarm\ndata: {json.dumps(data)}\n\n"""

        sleep(PENDING_TIME)
