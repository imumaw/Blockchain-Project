"""
 * Groupname: Definitely CS Majors

    SOFTWARE ENGINEERS: 
        Isaiah Mumaw        (imumaw@nd.edu)
        Ed Stifter          (estifter@nd.edu)
        Peter Ainsworth     (painswor@nd.edu)
        Adam Mazurek        (amazure2@nd.edu)
        
    PROJECT MANAGER:
        Julia Buckley       (jbuckle2@nd.edu)

    PROJECT DIRECTOR:
        Matt morrison       (matt.morrison@nd.edu)
    
 * Filename: block_lib.py
 * Date Created: 4/13/21 (last modified 4/14/21)
 * File Contents: Contains classes for simple blockchain implementation
"""

###############################################################################

#hashing function
from hashlib import sha256

###############################################################################

class Blockchain:
    """
    Class for management of entire blockchain.
    
    Functions:
        __init__ : initializes blockchain
            Parameters:
                None
            Returns:
                None
                
        add_block : adds a block to blockchain
            Parameters:
                transactions (list, optional) - list of transactions stored by block. Must be of transaction class. If not given, defaults to []
            Returns:
                None
                
        print_chain : prints all data stored within blockchain <INCOMPLETE>
            Parameters:
                None
            Returns:
                None
    
    Private Members:
        __blocks : all blocks contained within blockchain
    """

    def __init__( self, in_difficulty ):
        
        #initialize empty list of blocks and difficulty as private members (DO NOT REMOVE UNDERSCORES)
        #while Python doesn't completely prevent private member access, this is more secure
        self.__blocks = []
        self.__difficulty = in_difficulty
        
    def add_block( self, transactions=[] ):
        
        #get previous block and hash by accessing last list element
        prev_block = self.__blocks[-1]
        prev_hash = prev_block.hash
        
        #create new block using hash from previous block
        new_block = Block( transactions, prev_hash )
        
        #add new block to blockchain
        self.__blocks.append( new_block )
        
        return

    def proof_of_work(self, block): 
        # returns proof (i.e. hash) for new block to be inserted
        block.nonce = 0

        # increments nonce until hash meets requirements in brute force style
        computed_hash = block.compute_hash()
        while not(computed_hash.startswith('0' * self.__difficulty)):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def print_chain( self ):        #placeholder for future implementation
        
        return

###############################################################################

class Block:
    """
    Class for single block in blockchain.
    
    Functions:
        __init__ : initializes a Block
            Parameters:
                transactions (list, optional) - list of transactions stored by block. Must be of transaction class. If not given, defaults to []
                prev_hash (string, optional) - string storing previous hash. If no hash is given, defaults to "ROOT"
            Returns:
                None
        
        print_block : prints information stored in Block <INCOMPLETE>
            Parameters:
                None
            Returns:
                None

    Public Members:
        prev_hash : hash of previous block
        transactions : list of transactions stored by block. Must be of transaction class.
        data : string containing all block data (used to generate hash)
        hash : block hash generated using data
    """
    
    def __init__( self, transactions = [], prev_hash="ROOT" ):
        
        #set basic members
        self.prev_hash = prev_hash
        self.transactions = transactions
        
        #initialize block data using previous hash
        self.data = prev_hash
        
        #get block data as single string
        for i in range( len(transactions) ):
            curr_transaction = transactions[i]          #get current transaction
            self.data += " | "                          #add gap between elements
            self.data += curr_transaction.get_str()     #get string of current transaction
            
        #get hash using hashlib
        self.hash = sha256( self.data.encode() ).hexdigest()
        
    def print_block( self ):        #placeholder for future implementation
        
        return
    
###############################################################################