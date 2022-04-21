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
        Matt Morrison       (matt.morrison@nd.edu)
    
 * Filename: block_lib.py
 * Date Created: 4/13/21
 * File Contents: Contains classes for simple blockchain implementation
"""

###############################################################################

#hashing function
from hashlib import sha256

#record message time
import datetime

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
                
        proof_of_work : gets the hash of the next block to be inserted
            Parameters:
                <>
            Returns:
                <>
                
        print_chain : prints all data stored within blockchain <INCOMPLETE>
            Parameters:
                None
            Returns:
                None
        
        html : return an html representation of a chain with styling included.
            Parameters:
                <>
            Returns:
                <>
    
    Private Members:
        __blocks : all blocks contained within blockchain
    """

    def __init__( self, in_difficulty ):
        
        #initialize empty list of blocks and difficulty as private members (DO NOT REMOVE UNDERSCORES)
        #while Python doesn't completely prevent private member access, this is more secure
        self.__blocks = []
        self.__difficulty = in_difficulty
        
    def add_block( self, messages=[] ):
        
        #if we don't have a previous block we have a default hash
        if len(self.__blocks)==0:
            prev_hash = "ROOT"
        
        #get previous block and hash by accessing last list element
        else:
            prev_block = self.__blocks[-1]
            prev_hash = prev_block.hash
        
        #create new block using hash from previous block
        new_block = Block( messages, prev_hash )
        
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

    def print_chain( self, block_width=60 ):        #placeholder for future implementation
        
        #print the start of the chain
        output = "START OF BLOCKCHAIN\n"
    
        #iterate through all blocks
        for block in self.__blocks:
            
            output += "⇩⇩⇩⇩⇩\n"     #connect the blocks together
            output += block.print_block( block_width )      #call the print function for the block and append to the output string
    
        return output

    def html(self):

        html_string = ""

        for block in self.__blocks:
            html_string += '<div style="padding: 25px">' + block.html() + '</div>'
            html_string += '<div style="font-size: 24px; text-align: center;">&#8595;&#8595;&#8595;&#8595;</div>'

        return html_string

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
        messages : list of messages stored by block. Must be of transaction class.
        data : string containing all block data (used to generate hash)
        hash : block hash generated using data
    """
    
    def __init__( self, messages = [], prev_hash="ROOT" ):
        
        #set basic members
        self.prev_hash = prev_hash
        self.messages = messages
        
        #initialize block data using previous hash
        self.data = prev_hash
        
        #get block data as single string
        for i in range( len(self.messages) ):
            curr_message = self.messages[i]          #get current transaction
            self.data += " | "                          #add gap between elements
            self.data += curr_message.print_message()     #get string of current transaction
            
        #get hash using hashlib
        self.hash = sha256( self.data.encode() ).hexdigest()
        
    def print_block( self, block_width=60 ):
        
        #this will prevent errors
        if block_width < 10:
            block_width = 10
        
        #set up characters to build border around block
        up_border = "┏"+("━"*(block_width-2))+"┓"
        lside = "┃ "
        rside = " ┃"
        dn_border = "┗"+("━"*(block_width-2))+"┛"
        
        #empty line to go above and below each message
        pad_line = lside+(" "*(block_width-4))+rside
        
        #hash of block to go at top
        title = "BLOCK HASH: " + str(self.hash)
        
        #the actual block will look something like this (this example has default width):
        """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                                         ┃
        ┃ From: Dr. Morrison                                      ┃
        ┃ To: Definitely CS Majors Group                          ┃
        ┃ At: 2022-05-01:T16:34:04+00:00                          ┃
        ┃ Message:                                                ┃
        ┃    Wow, this block is decently formatted.               ┃
        ┃                                                         ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """
        
        output = up_border + "\n"
        output += self.gen_line( title, block_width, lside, rside )
        
        for message in self.messages:
            output += pad_line + "\n"
            message_elements = message.print_message().splitlines()
            
            output += self.gen_line( message_elements[0], block_width, lside, rside )
            output += self.gen_line( message_elements[1], block_width, lside, rside )
            output += self.gen_line( message_elements[2], block_width, lside, rside )
            output += self.gen_line( message_elements[3], block_width, lside, rside )
            output += self.gen_line( message_elements[4], block_width, lside+"    ", rside )
        
        output += pad_line + "\n"
        output += dn_border + "\n"
        
        return output
    
    
    def gen_line( self, string, width, lborder, rborder ):
        
        line = lborder + string
        output = ""
        
        i = 0
        for char in line:
            
            if char=="\n":
                while i<(width-len(rborder)):
                    i += 1
                    output += " "
                    
                output += rborder + "\n" + lborder 
                i=len(lborder)
            
            else:
    
                if i==len(lborder) and char==" ":
                    pass
                    
                else:
                    i+=1
                    output+=char
            
                if i==width-len(rborder):
                    
                    output += rborder + "\n" + lborder 
                    i=len(lborder)
                
            
                
        while i<(width-len(rborder)):
            i += 1
            output += " "
            
        output += rborder + "\n"
            
        return output

    def html(self):
        """Return an html representation of a block with styling included."""

        html_string = '<div style="padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, .1);">'
        html_string += f'<div style="font-size: 1rem; font-weight: bold; font-family: monospace; text-align: center;">Block Hash: {self.hash}</div>'
        
        for message in self.messages:
            html_string += '<div style="margin-top: 40px">' + message.html() + '</div>'

        html_string += "</div>"
        return html_string
    
###############################################################################

class Message:
    """
        Message holds a few pieces of data about a message between 2 users and is similar to an email.

        It contains:
            - The message's sender
            - The message's receiver
            - The time of message
            - The actual message
    """

    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time = datetime.datetime.now()

    def print_message(self):
        
        #Output format:
            
        #From: <sender>
        #To: <receiver>
        #At: <date and time>
        #Message:
        #   <message content>
        
        m_format = """From: {the_sender}
        To: {the_receiver}
        At: {the_time}
        Message:
            {the_message}"""
        
        return m_format.format( the_sender = self.sender, the_receiver = self.receiver, the_time = self.time.isoformat(), the_message = self.message)

    def html(self):
        """Return an html representation of a message with styling included."""

        return f"""
            <div style='font-family: sans-serif;'>
                <ul style='list-style-type: none; margin: 10px; padding: 5px; border-bottom: 1px solid lightgray; border-top: 1px solid lightgray;'>
                    <li>
                        <span style="display: inline-block; min-width: 50px; font-weight: bold;">From:</span>
                        <span style="flex: 10; font-weight: bold;">{self.sender}</span>
                    </li>
                    <li>
                        <span style="display: inline-block; min-width: 50px;">To:</span>
                        <span style="flex: 10;">{self.receiver}</span>
                    </li>
                    <li>
                        <span style="display: inline-block; min-width: 50px;">At:</span>
                        <span style="flex: 10;">{self.time.strftime('%a, %b %d, %Y %I:%M%p')}</span>
                    </li>
                </ul>
                <p style='margin-left: 15px;'>
                    {self.message}
                </>
            </div>
        """
