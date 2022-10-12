from multiprocessing import process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":

    processes = []
    num_processes = os.cpu_count()
# number of cpus on the machine.
#usually a good choice for the number of processes

#create processes and asign a func for each process
    for i in range(num_processes):
        p = process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

#wait for all processes to finish
#block the main program until these processes are finished
    for p in processes:
        p.join()

print('end main')

