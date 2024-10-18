import random
import time
from threading import Thread
from threading import Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            number = random.randint(50,500)
            self.balance += number
            print(f'Пополнение: {number}. Баланс: {self.balance}\n')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for k in range(100):
            number = random.randint(50, 500)
            print(f'Запрос на {number}\n')
            if number <= self.balance:
                self.balance -= number
                print(f'Снятие: {number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

if __name__ == '__main__':
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk, ))
    th2 = Thread(target=Bank.take, args=(bk, ))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
