"""
This DB class is not thread safe.
How can we make this thread safe?
"""

import time

import concurrent.futures

class FakeDatabase:

    def __init__(self):
        self.value = 0

    def update(self, name):
        print(f"Thread {name}: starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(2)
        self.value = local_copy
        print(f"Thread {name} finishing update")



if __name__ == "__main__":

    database = FakeDatabase()
    print(f"Testing update. Starting value is {database.value}.", )

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
            
    print(f"Testing update. Ending value is {database.value}.")
