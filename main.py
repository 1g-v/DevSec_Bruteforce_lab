import multiprocessing as mp
from hashlib import sha256
import itertools
import time

alpha = "abcdefghijklmnopqrstuvwxyz"
with open("sha.txt") as file:
    array = [row.strip() for row in file]


def crack_sha256_hashes(alpha_bit):
    for i in itertools.product(alpha_bit, alpha, alpha, alpha, alpha):
        if sha256(''.join(i).encode('utf-8')).hexdigest() in array:
            print('Password for the hash function ' + sha256(''.join(i).encode('utf-8')).hexdigest() + ' - ' + ''.join(i))


def input_threads():
    while True:
        max_threads = mp.cpu_count()
        number = int(input(f"Enter the threads used in range [1, {max_threads}]: "))
        if number in range(1, max_threads + 1):
            return number
        else:
            print("Try again.")


if __name__ == '__main__':
    procs = []
    threads_count = input_threads()
    parts_count = len(alpha) // threads_count
    start = time.perf_counter()
    for i in range(threads_count):
        if i == threads_count - 1:
            bit = alpha[parts_count * i:]
        else:
            bit = alpha[parts_count * i:parts_count * (i + 1)]
        p = mp.Process(target=crack_sha256_hashes, args=(bit,))
        procs.append(p)
        p.start()
    [proc.join() for proc in procs]
    stop = time.perf_counter()
    input(f"\nThe calculation took {stop - start:0.4f} seconds, used {threads_count} thread(s).\n\nPress Enter to exit...")