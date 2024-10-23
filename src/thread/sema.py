import threading as th
import time
import random
from queue import Queue

# 버퍼 크기를 제한하는 세마포어
empty = th.Semaphore(5)  # 최대 5개 항목
full = th.Semaphore(0)  # 초기에는 비어있음
mutex = th.Semaphore(1)  # 상호 배제를 위한 세마포어

buffer = Queue()


def producer(name: str):
    for i in range(10):
        empty.acquire()  # 빈 공간 확보
        mutex.acquire()  # 버퍼 접근 권한 획득

        item = f"Item {i}"
        buffer.put(item)
        print(f"{name} produced {item}")

        mutex.release()  # 버퍼 접근 권한 해제
        full.release()  # 채워진 공간 알림

        time.sleep(random.uniform(0.1, 0.5))


def consumer(name: str):
    while True:
        full.acquire()  # 채워진 공간 대기
        mutex.acquire()  # 버퍼 접근 권한 획득

        try:
            item = buffer.get_nowait()
            print(f"{name} consumed {item}")
        except Queue.Empty:
            break
        finally:
            mutex.release()  # 버퍼 접근 권한 해제
            empty.release()  # 빈 공간 알림

        time.sleep(random.uniform(0.2, 0.7))


if __name__ == "__main__":
    producers = [th.Thread(target=producer, args=(f"Producer {i}",)) for i in range(2)]
    consumers = [th.Thread(target=consumer, args=(f"Consumer {i}",)) for i in range(3)]

    # 모든 스레드 시작
    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    # 모든 스레드 종료 대기
    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    print("Production and consumption completed")
