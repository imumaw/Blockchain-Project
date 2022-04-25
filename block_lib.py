#! /usr/bin/env python3
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
###############################################################################
###############################################################################

#record message time
import datetime
import hashlib

###############################################################################
###############################################################################
###############################################################################

class Blockchain:
    
    """
    Class for management of entire blockchain.
    
    Public Functions:
        __init__ : initializes blockchain
            Parameters:
                None
            Returns:
                None
                
        add_block : adds a block to blockchain
            Parameters:
                block (Block class) - empty block
                proof ( hex ) - proof of work hash
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
        
        html : get an html representation of a chain with styling included.
            Parameters:
                None
            Returns:
                html_string - string containing html code for website
    
    Public Members:
        unconfirmed_messages : list of all messages not yet stored in blocks, accessed in FIFO order
    
    Private Members:
        __blocks : all blocks contained within blockchain
        __dificulty : length of hash to compute, longer hashes take longer to compute thus increasing the mining time
    """
    
    ###########################################################################

    def __init__( self, in_difficulty ):
        
        #initialize empty list of blocks and difficulty as private members (DO NOT REMOVE UNDERSCORES)
        #while Python doesn't completely prevent private member access, this is more secure
        self.__blocks = []
        self.__difficulty = in_difficulty
        self.unconfirmed_messages = []
        self.add_genesis_block()
    
    ###########################################################################

    def add_genesis_block(self):
        genesis_block = Block()
        self.__blocks.append(genesis_block)

    ###########################################################################
      
    def add_block( self, block, hash ):
        
        # check new block matches last hash in chain
        last_hash = self.__blocks[-1].hash
        if block.prev_hash != last_hash:
            return False
        
        # checks if new block hash is valid
        if not self.valid_hash(block, hash):
            return False

        block.hash = hash
        self.__blocks.append(block)
        return True
        

    ###########################################################################

    def proof_of_work(self, block): 

        block.nonce = 0

        # increments nonce until hash meets requirements in brute force style
        computed_hash = block.compute_hash()
        while not(computed_hash.startswith('0' * self.__difficulty)):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    ###########################################################################
    
    def valid_hash(self, block, hash):
        """
        Checks if hash is correct and satisfies difficulty
        Returns True on succuss, false on failure
        """
        if not hash.startswith('0' * self.__difficulty):
            return False

        if hash != block.compute_hash():
            return False

        return True

    ###########################################################################

    def mine (self):
        """
        Adds pending transactions to the blockchain by solving proof-of-work and confirming messages
        returns hash of new block upon success
        returns false on failure
        """

        if self.unconfirmed_messages == []:
            return False

        prev_block = self.__blocks[-1].hash
        block = Block(messages=self.unconfirmed_messages, prev_hash=prev_block)
        self.unconfirmed_messages = []
        new_hash = self.proof_of_work(block)

        if not self.add_block(block, new_hash):
            return False

        return new_hash

    ###########################################################################

    def print_chain( self, block_width=60 ):
        
        #print the start of the chain
        output = "START OF BLOCKCHAIN\n"
    
        #iterate through all blocks
        for block in self.__blocks:
            
            output += "⇩⇩⇩⇩⇩\n"     #connect the blocks together
            output += block.print_block( block_width )      #call the print function for the block and append to the output string
    
        return output

    ###########################################################################

    def html(self):

        #init with empty string
        html_string = ""

        #go through blocks and get html for each, appending to string
        for block in self.__blocks:
            html_string += '<div style="padding: 25px">' + block.html() + '</div>'
            html_string += '<div style="font-size: 24px; text-align: center;">&#8595;&#8595;&#8595;&#8595;</div>'

        return html_string

###############################################################################
###############################################################################
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
        
        print_block : prints messages stored in Block. Also creates a border around the block
            Parameters:
                block_width (int, optional) - width of block in chars. Defaults to 60.
            Returns:
                output (string) - string
                
        __gen_line (PRIVATE) : creates an individual line of Block output, formatted to look all nice
            Parameters:
                string (string) - the unaltered line of output from the Message
                width (int) - width of block to be produced
                lborder (string) - left side border of block
                rborder (string) - right side border of block
            Returns:
                output (string) - string of output which is formatted to match the block
                
        html : get an html representation of a block with styling included.
            Parameters:
                None
            Returns:
                html_string - string containing html code for website

    Public Members:
        prev_hash (hex) - hash of previous block
        messages (list of Message class) - list of messages stored by block. Must be of transaction class.
        hash (hex) - block hash generated using data
        nonce (int) - number only use once
    """
    
    ###########################################################################
    
    def __init__( self, messages = [], prev_hash="ROOT" ):
        
        #set basic members
        self.hash = 0x0
        self.prev_hash = prev_hash
        self.messages = messages
        self.nonce = 0

    ###########################################################################


    def compute_hash( self ):
        """
        Returns hash of block contents
        """

        #initialize block data using previous hash
        self.data = str(self.prev_hash)

        #get block data as single string
        for i in range( len(self.messages) ):
            curr_message = self.messages[i]          #get current transaction
            self.data += " | "                          #add gap between elements
            self.data += curr_message.print_message()     #get string of current transaction

        # add nonce val to end of data string
        self.data += str(self.nonce)

        #get hash using hashlib
        return hashlib.sha256(self.data.encode()).hexdigest()

    
    ###########################################################################
    
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
        
        #create title of block
        output = up_border + "\n"
        output += self.gen_line( title, block_width, lside, rside )
        
        #iterate through messages
        for message in self.messages:
            
            #pad the space above the message
            output += pad_line + "\n"
            
            #call print_message and split between each line
            message_elements = message.print_message().splitlines()
            
            #append to output using gen_line on each message element
            for i in range( len(self.messages) ):
                
                #information lines are not indented
                if i<4:
                    output += self.__gen_line( message_elements[i], block_width, lside, rside )
                    
                #message lines are indented so we increase the left side border.
                #this also accounts for edge cases where the message has multiple paragraphs
                else:
                    output += self.__gen_line( message_elements[i], block_width, lside+"    ", rside )
        
        #pad the bottom of the block and add the border
        output += pad_line + "\n"
        output += dn_border + "\n"
        
        return output
    
    ###########################################################################
    
    def __gen_line( self, string, width, lborder, rborder ):
        
        #initialize variables
        line = lborder + string     #prevent extra work by appending the left border
        output = ""
        
        #index value is independent of the for loop
        i = 0
        
        #loop through each character in the line
        for char in line:
            
            #in the case where we encounter a newline character
            if char=="\n":
                
                #pad with spaces and move index
                while i<(width-len(rborder)):
                    i += 1
                    output += " "
                
                #end line and create new line
                output += rborder + "\n" + lborder 
                i=len(lborder)
            
            #in every other case -- no newline character
            else:
    
                #if we encounter a space and we're at the beginning we can skip it
                if i==len(lborder) and char==" ":
                    pass
                 
                #otherwise we'll append the character
                else:
                    i+=1
                    output+=char
            
                #if we're at the end of the line...
                if i==width-len(rborder):
                    
                    #add border and newline and border
                    output += rborder + "\n" + lborder 
                    
                    #reset index
                    i=len(lborder)
                
        #now at the end of the line we pad it out        
        while i<(width-len(rborder)):
            i += 1
            output += " "
        
        #add the final border
        output += rborder + "\n"
            
        return output

    ###########################################################################

    def html(self):

        #create string of code and append the start of the block
        html_string = '<div style="padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, .1);">'
        html_string += f'<div style="font-size: 1rem; font-weight: bold; font-family: monospace; text-align: center;">Block Hash: {self.hash}</div>'
        
        #append each message's code to output
        for message in self.messages:
            html_string += '<div style="margin-top: 40px">' + message.html() + '</div>'

        #terminate
        html_string += "</div>"
        
        return html_string
    
###############################################################################
###############################################################################
###############################################################################

class Message:
    
    """
    Message holds a few pieces of data about a message between 2 users and is similar to an email.
    
    Functions:
        __init__ : initializes a Block
            Parameters:
                sender (string) - who is sending the message
                receiver (string) - who is getting the message
                message (string) - message content
            Returns:
                None
        
        print_block : prints message
            Parameters:
                None
            Returns:
                output (string) - string
                
        html : get an html representation of a block with styling included.
            Parameters:
                None
            Returns:
                html_string - string containing html code for website

    Public Members:
        sender (string) - who is sending the message
        receiver (string) - who is getting the message
        message (string) - message content
        time (string) - the time at which the message was sent
    """

    ###########################################################################

    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time = datetime.datetime.now()

    ###########################################################################

    def print_message(self):
        
        m_format = """From: {the_sender}
        To: {the_receiver}
        At: {the_time}
        Message:
            {the_message}"""
        
        return m_format.format( the_sender = self.sender, the_receiver = self.receiver, the_time = self.time.isoformat(), the_message = self.message)

    ###########################################################################

    def html(self):

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
