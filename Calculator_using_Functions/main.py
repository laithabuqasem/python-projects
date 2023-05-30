
#Calculator

#Add
def add(n1,n2):
    """Adds the two given values: n1, n2 and returns the value"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """Subtracts the two given values: n1, n2 and returns the value"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Multiplies the two given values: n1, n2 and returns the value"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """Divides the two given values: n1, n2 and returns the value"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}