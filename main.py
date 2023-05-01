import string
import multiprocessing as mp
from hashlib import sha256
import itertools
import time

alpha = string.ascii_lowercase
with open("sha.txt") as file:
    array = [row.strip() for row in file]


def f(alpha_bit):
    for i in itertools.product(alpha_bit, alpha, alpha, alpha, alpha):
        if sha256(''.join(i).encode('utf-8')).hexdigest() in array:
            print('Password for the hash function ' + sha256(''.join(i).encode('utf-8')).hexdigest() + ' - ' + ''.join(i))


def input_streams():
    while True:
        number = int(input("Enter the streams used in range [1, 25]: "))
        if number in range(1, 26):
            return number
        else:
            print("Try again.")


if __name__ == '__main__':
    procs = []
    streams_count = input_streams()
    parts_count = len(alpha) // streams_count
    start = time.perf_counter()
    for i in range(streams_count):
        if i == streams_count - 1:
            bit = alpha[parts_count * i:]
        else:
            bit = alpha[parts_count * i:parts_count * (i + 1)]
        p = mp.Process(target=f, args=(bit,))
        procs.append(p)
        p.start()
    [proc.join() for proc in procs]
    stop = time.perf_counter()
    input(f"\nThe calculation took {stop - start:0.4f} seconds, used {streams_count} stream(s).\n\nPress Enter to exit...")
