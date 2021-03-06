import random
from queues.queue import Queue

"""
Algorithm
    1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival.
        The queue is empty to estart
    
    2. For each seconds(current_second):
        - Does a new print task get created? If so, add it to the queue with the current_seconds
            as the timestamp.
        - If the printer is not busy if a task is waiting,
            - Remove the next task from the print queue and assign it to the printer.
            - Substract the timestamp from the current_second to compute the waiting time
                for that task.
            - Append the waiting time for that task to a list for later processing.
            - Based on the number of pages in the print task, figure out how much will be required
        - The printer now does one second of printing if necessary. It also substract one second
            from the time required for that task
        - If the task has been completed, in other words the time required has reached zero, the
            printer is no longer busy.

Student => Printer => Task => Paper => 1 to 20 pages length
"""



class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / (self.page_rate * 2)


class Task:
    def __init__(self, time):
        self.timestamp = time
        # Hardcoded
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_print_task(secondsPerTask):
    num = random.randrange(1, secondsPerTask+1)
    if num == secondsPerTask:
        return True
    else:
        return False


def simulation(num_seconds, pages_per_minute, students):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    tasks = students * 2
    seconds_per_stask = tasks*9

    for current_second in range(num_seconds):
        if new_print_task(seconds_per_stask):
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy() and (not print_queue.is_empty())):
            new_task = print_queue.dequeue()
            waiting_times.append(new_task.wait_time(current_second))
            lab_printer.start_next(new_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining"
          % (average_wait, print_queue.size()))


for i in range(10):
    simulation(3600, 5, 20)
