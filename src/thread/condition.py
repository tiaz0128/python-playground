import threading as th
import time

condition = th.Condition()
data = []


def producer():
    for i in range(1, 6):
        with condition:
            data.append(i)
            print(f"생산: {i}")
            condition.notify()  # 소비자에게 알림
            time.sleep(1)  # 생산 시간 간격


def consumer():
    while len(data) < 5:  # 5개 데이터를 모두 소비할 때까지
        with condition:
            if not data:  # 데이터가 없으면
                condition.wait()  # 생산자 대기
            value = data.pop(0)
            print(f"소비: {value}")


producer_thread = th.Thread(target=producer)
consumer_thread = th.Thread(target=consumer)

if __name__ == "__main__":
    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
    print("Done")
