# What is a blockchain?

A [blockchain](https://en.wikipedia.org/wiki/Blockchain) is a list of records that are linked together using cryptography. The idea behind a blockchain is that each new block added to the chain contains a hash of the previous block, so it would be impossible to change one block without breaking the entire chain. In order to fully understand this process, we will have to cover a few important topics.

## Hashing

Hashing is an essential part of blockchains that ensures security of the chain. It is a process by which some more complicated object can be represented in a simple form. There are many types of hashing algorithms with different properties, but the one most often used in blockchains is called SHA256. Let's see how it works.

```python
from hashlib import sha256

sha256("Hello World!".encode()).hexdigest()
>>> '7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069'

sha256("Hello World".encode()).hexdigest()
>>> 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
```

Notice how simply removing the exclamation point completely changes the hash? This is what makes hashing so useful in blockchain! Any slight change in the data of a block would change its hash, and since part of the next block is the previous hash, any change in one block would have to propogate down the whole chain in order to go unnoticed. We can see then that hashing the blocks gives us a good way to ensure that nothing in our chain has been changed without someone noticing.

## Proof of Work

Proof of work is another part of several popular blockchains (like Bitcoin). It is what prevents bad actors from altering transaction history on the chain without someone noticing. As the original Bitcoin whitepaper puts it, the truth is essentially set by "the largest pool of CPU power."

Proof of work can take many forms, but the idea is the same. There should be something unknown that takes lots of CPU power to find, and once it is found, a block can be added to the blockchain. 

Our blockchain's proof-of-work design is taken from [Bitcoin's](https://bitcoin.org/bitcoin.pdf). The general strategy is to find a number (typically called a nonce) such that, when added to the hash of a block, the first several bits of the hash are 0s. Over time, (i.e., as computing power increases) the number of 0s which are required will increase. Here is a contrived example:

_Note: the code here is Python pseudocode and will not necessarily work in its current form._
```python
from hashlib import sha256

class Block:
    ...

    def hash(self):
        # add nonce to data of block
        block_hash = str(self.data) + str(self.nonce)

        # return the hashed data+nonce value
        return sha256(block_hash.encode()).hexdigest()

class Chain:
    proof_difficulty = 1
    ...

    def proof_of_work(self, block):
        # ensure nonce starts at 0
        block.nonce = 0

        # check for the leading zeros in the hash
        while not block.hash().startswith('0' * self.proof_difficulty):
            block.nonce += 1
```

Here we see that the proof-of-work strategy is pure brute-force, so those with the largest amount of CPU power should be able to find the correct nonce first and outpace bad actors. 

Without such proof-of-work, it would be possible for attackers to substitute their own blockchain for the actual chain at minimal cost. Perhaps their chain would show them receiving millions of Bitcoin, making them rich. 

It is important to note that most proof-of-work (and definitely Bitcoin) relies on most CPU power being in the hands of honest people. The first node to complete the proof-of-work gets to add the block and thus 'set the truth' of the chain. If a bad actor had enough CPU power to outpace everyone else, they could 'set the truth' to be whatever they wanted it to be.

## Multiple Nodes

The final important part of most blockchains is that they are distributed. This means that multiple computers work together to operate the chain so that if one goes down, the entire chain does not go down.

In essence, every transaction by a user of the chain is sent to each node (computer) on the chain. Each node then works to compute a proof-of-work fastest, and the first to complete it sends the result to each other node. The other nodes then all check the validity of each hashed block themselves, making sure that each block's hash corresponds to the previous block's hash. Then nodes go to work on the proof-of-work for the next block, restarting the cycle.