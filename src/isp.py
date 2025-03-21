# Naruszona zasada ISP

from abc import ABC, abstractmethod


class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class IEater(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(IWorker, IEater):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")


class RobotWorker(IWorker):
    def work(self):
        print("Robot worker working")


# Usage
human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()
robot.work()
