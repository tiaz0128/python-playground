import threading as th
from queue import Queue, Empty
import time


def producer(queue: Queue):
    for i in range(1, 6):
        queue.put(i)  # 큐에 데이터 추가
        print(f"생산: {i}")
        time.sleep(1)


def consumer(queue: Queue):
    while True:
        try:
            value = queue.get(timeout=5)  # 5초 동안 대기
            print(f"소비: {value}")
            queue.task_done()
        except Empty as e:
            print("소비자 종료")
            break


queue = Queue()
producer_thread = th.Thread(target=producer, args=(queue,))
consumer_thread = th.Thread(target=consumer, args=(queue,))

if __name__ == "__main__":
    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
    print("Done")
