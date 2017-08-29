
Variable to (un)marshall: a lorem ipsum written in lorem.txt

The run() method is the following:
|def run( self ):
|        """Creates a variable, marshalls it, then unmarshalls it."""
|        with open("lorem.txt", "r") as myFile:
|            lorem_ipsum = myFile.read()
|        marshall_test = DEncode.encode(lorem_ipsum)
|        unmarshall_test = DEncode.decode(marshall_test)

Number of clients:
20000; 40000; 60000; 80000; 100000; 120000; 140000; 160000; 180000; 200000
