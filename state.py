from abc import ABC, abstractmethod

class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.current = []
        self.status = Locked()

    def set_state(self, state):
        self.status = state

    def enter_digit(self, digit):
        self.status.enter_digit(self, digit)


# --- STATE BASE ---
class Status(ABC):
    @abstractmethod
    def enter_digit(self, lock, digit):
        pass


# --- LOCKED ---
class Locked(Status):
    def __init__(self):
        print("lukk lukus")

    def enter_digit(self, lock, digit):
        lock.current.append(digit)

        # kontrolli prefixit (mitte ainult täielikku võrdlust!)
        if lock.current != lock.combination[:len(lock.current)]:
            lock.set_state(Error())
        elif lock.current == lock.combination:
            lock.set_state(Unlocked())


# --- UNLOCKED ---
class Unlocked(Status):
    def __init__(self):
        print("lukk lahti")

    def enter_digit(self, lock, digit):
        print("lukk on juba lahti, sisendit ei arvestata")

    def lock(self, lock):
        print("lukk läheb lukku")
        lock.current = []
        lock.set_state(Locked())


# --- ERROR ---
class Error(Status):
    def __init__(self):
        print("vale kombinatsioon")

    def enter_digit(self, lock, digit):
        print("vale olek, eemaldan viimase sisendi")
        if lock.current:
            lock.current.pop()

        lock.set_state(Locked())

cl = CombinationLock([1, 2, 3, 4, 5])
print(cl.status)
 
cl.enter_digit(1)
print(cl.status)
 
cl.enter_digit(2)
print(cl.status)

cl.enter_digit(3)
print(cl.status)

cl.enter_digit(4)
print(cl.status)

cl.enter_digit(5)
print(cl.status)
