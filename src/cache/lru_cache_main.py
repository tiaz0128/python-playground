from time import sleep
from functools import lru_cache
from progress_bar import ProgressBar


@lru_cache(maxsize=100)
def expensive_function(sleeping_time):
    sleep(sleeping_time)

    return "test"


if __name__ == "__main__":
    sleeping_times = [5, 3, 3, 5]

    with ProgressBar(sleeping_times, "Processing expensive functions") as pbar:
        for time in sleeping_times:
            expensive_function(time)
            pbar.update(1)
