import threading as th


class CustomEvent:
    def __init__(self):
        self.event1 = th.Event()
        self.event2 = th.Event()
        self.count = 0


def worker1(custom_event: CustomEvent):
    for i in range(1, 6):
        print(f"Worker 1: {i}")
        custom_event.count += 1
        if custom_event.count >= 3:
            custom_event.event1.set()  # 카운트가 3 이상이면 이벤트1 발생


def worker2(custom_event: CustomEvent):
    custom_event.event1.wait()  # 이벤트1 대기
    print("Worker 2: Started after count >= 3")
    for i in range(1, 4):
        print(f"Worker 2: {i}")
    custom_event.event2.set()  # 작업 완료 후 이벤트2 발생


def worker3(custom_event: CustomEvent):
    custom_event.event2.wait()  # 이벤트2 대기
    print("Worker 3: Started after Worker 2 finished")
    for i in range(1, 4):
        print(f"Worker 3: {i}")


custom_event = CustomEvent()
t1 = th.Thread(target=worker1, args=(custom_event,))
t2 = th.Thread(target=worker2, args=(custom_event,))
t3 = th.Thread(target=worker3, args=(custom_event,))

if __name__ == "__main__":
    t1.start()
    t2.start()
    t3.start()

    t3.join()
    print("Done")
