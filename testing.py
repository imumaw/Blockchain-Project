import block_lib as blib

chain = blib.Blockchain(3)

message1 = blib.Message( "Dr. Morrison", "Definitely CS Majors Group", "Wow this is decently formatted" )
messages1 = [message1]

chain.add_block( messages1 )

message2 = blib.Message( "Definitely CS Majors Group", "Dr. Morrison", "Thank you professor!" )
message3 = blib.Message( "Definitely CS Majors Group", "Dr. Morrison", "Here's hoping for that gift card prize!" )
messages2 = [message2, message3]

chain.add_block( messages2 )

print( chain.print_chain(block_width=60) )