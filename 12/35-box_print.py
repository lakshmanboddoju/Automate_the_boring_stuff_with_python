#! python3

"""

Prints out a box of the following type for a specified argument list:


***************
*             *
*             *
*             *
*             *
***************


"""

def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('The "symbol" needs to be a 1 character string.')

    if (width < 2) or (height < 2):
        raise Exception('The "width" and "height" must be greater or equal to 2.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print (symbol * width)

boxPrint('.', 10, 5)
