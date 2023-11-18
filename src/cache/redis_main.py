from time import sleep
import redis
from progress_bar import ProgressBar


def expensive_function(sleeping_time):
    sleep(sleeping_time)

    return "test"


# Redis 연결 설정
def create_redis_connection(host: str, port: int, db: int) -> redis.Redis:
    return redis.Redis(host=host, port=port, db=db)


if __name__ == "__main__":
    r = create_redis_connection("localhost", 6379, 0)

    sleeping_times = [5, 3, 3, 5]

    with ProgressBar(sleeping_times, "Processing expensive functions") as pbar:
        for sleep_time in sleeping_times:
            redis_key = str(sleep_time)
            if not r.exists(redis_key):
                result = expensive_function(sleep_time)
                r.set(redis_key, result)
            else:
                result = r.get(redis_key)

            pbar.update(1)
