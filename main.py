# -----------------------------------------------------------
# This iis the main file.
#
# email -> mintu.giri1997@gmail.com
# -----------------------------------------------------------

### --- IMPORTS --- ###
from queue import Queue
from threading import Thread
from database import read_data
from process import pop_ten_elements, process_data
from time import time

class DataProcessor(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            data = self.queue.get()
            try:
                process_data(data)
            finally:
                self.queue.task_done()

# -----------------------------------------------------------
# main function
# -----------------------------------------------------------
def main():
    ts = time()
    datas = read_data("fake_data","UNPROCESSED")
    while len(datas) > 0:
        popped = pop_ten_elements(datas)
        queue = Queue()
        # Create 2 worker threads
        for x in range(2):
            worker = DataProcessor(queue)
            worker.daemon = True
            worker.start()
        queue.put((popped))
        queue.join()
    print(f"Took -> {time()-ts}")

if __name__ == '__main__':
    main()