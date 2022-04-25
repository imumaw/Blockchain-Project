#! /usr/bin/env python3

import block_lib as blib
import time

def main():
    difficulty = 6
    block_count = 10
    blockchain = blib.Blockchain(difficulty)
    i = 0

    while(i < block_count):
        
        start_time = time.time()
        new_hash = blockchain.mine()
        end_time = time.time()
        elapsed_time = end_time - start_time

        if new_hash:
            print("Block #" + str(i+1) + " added at hash: " + str(new_hash))

        print("Elapsed time: {:.2f} seconds".format(elapsed_time))
        print("--------------------------------------")

        i += 1

if __name__ == '__main__':
    main()