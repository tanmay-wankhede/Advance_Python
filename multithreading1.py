from threading import Thread, Lock
import time

database_value = 0

def increase():
    global database_value
    
    with Lock:
        local_copy = database_value
        local_copy += 1 
        time. sleep(0.1)
    
        database_value = local_copy
   

if __name__ == "_main_":

    lock = Lock()
    print('start value', database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start() 
    thread2.start()

    thread1.join() 
    thread2.join()

print('end value', database_value)

print('end main')
