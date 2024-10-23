import threading as th
from typing import Callable

# Event 객체 생성
event = th.Event()


def print_numbers1(name: str):
    for i in range(1, 11):
        print(f"{name} : {i}")
    event.set()  # Thread 1 완료 신호


def print_numbers2(name: str):
    event.wait()  # Thread 1 완료 대기
    for i in range(1, 11):
        print(f"{name} : {i}")


thread1 = th.Thread(target=print_numbers1, args=("Thread 1",))
thread2 = th.Thread(target=print_numbers2, args=("Thread 2",))

if __name__ == "__main__":
    thread1.start()
    thread2.start()

    thread2.join()
    print("Done")
