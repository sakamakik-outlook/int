import concurrent.futures
import time
from fake_db import FakeDatabase

if __name__ == "__main__":

    database = FakeDatabase()
    print(f"Testing update. Starting value is {database.value}.", )

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
            
    print(f"Testing update. Ending value is {database.value}.")
