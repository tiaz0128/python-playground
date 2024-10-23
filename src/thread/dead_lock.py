import threading as th
import time


class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.lock = th.Lock()


def transfer(from_account: BankAccount, to_account: BankAccount, amount: int):
    # 데드락 방지를 위해 항상 낮은 ID의 락을 먼저 획득
    first_lock = (
        from_account.lock if id(from_account) < id(to_account) else to_account.lock
    )
    second_lock = (
        to_account.lock if id(from_account) < id(to_account) else from_account.lock
    )

    with first_lock:
        with second_lock:
            if from_account.balance >= amount:
                from_account.balance -= amount
                time.sleep(0.1)  # 트랜잭션 지연 시뮬레이션
                to_account.balance += amount
                print(
                    f"Transferred {amount} from {from_account.name} to {to_account.name}"
                )
            else:
                print(f"Insufficient funds in {from_account.name}")


if __name__ == "__main__":
    account1 = BankAccount(1000, "Account 1")
    account2 = BankAccount(1000, "Account 2")

    # 동시에 양방향 이체 시도
    t1 = th.Thread(target=transfer, args=(account1, account2, 500))
    t2 = th.Thread(target=transfer, args=(account2, account1, 300))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(
        f"Final balances: {account1.name}: {account1.balance}, {account2.name}: {account2.balance}"
    )
