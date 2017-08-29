
Variable to (un)marshall: long(12345678910)

The run() method is the following:
|def run( self ):
|    test_long = long(12345678910)
|    marshall_test = DEncode.encode(test_long)
|    unmarshall_test = DEncode.decode(marshall_test)

Number of clients:
50000; 100000; 150000; 200000; 250000; 300000; 350000; 400000; 450000; 500000
