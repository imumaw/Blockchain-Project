#! /usr/bin/env python3

import block_lib as blib
import secrets
import time

def main():
    difficulty = 1
    blockchain = blib.Blockchain(difficulty)

    messages = [blib.Message(sender="anon", receiver="anon", message=secrets.token_hex(x)) for x in range(10)]

    for message in messages:
        blockchain.add_message(message)
        time.sleep(1)

if __name__ == '__main__':
    main()
