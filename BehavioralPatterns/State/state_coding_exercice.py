class CombinationLock:
    def __init__(self, combination):
        self.status = "LOCKED"
        self.combination = ''.join(str(x) for x in combination)

    def reset(self):
        self.status = "LOCKED"

    def enter_digit(self, digit):
        if self.status == "LOCKED":
            self.status = str(digit)
        else:
            self.status += str(digit)
            if not self.combination.startswith(self.status):
                self.status = "ERROR"
            if self.status == self.combination:
                self.status = "OPEN"


if __name__ == "__main__":
    lock = CombinationLock([1, 2, 3, 4, 5])

    lock.enter_digit(1)
    lock.enter_digit(2)
    lock.enter_digit(3)
    lock.enter_digit(4)
    lock.enter_digit(5)

    print(lock.status)

    lock.reset()

    print(lock.status)
