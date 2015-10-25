#Programmer: Alfredo Yebra
#Date:       October 3, 2015

class ALU:
    def __init__(self):
        self.alu_ops = {
            'ADD': lambda a, b: round(a + b, 2),  #Add
            'SUB': lambda a, b: round(b - a, 2),  #Subtract
            'DIV': lambda a, b: round(b / a, 2),  #Divide
            'MUL': lambda a, b: round(a * b, 2),  #Multiply
            'AND': lambda a, b: a & b,            #Bitwise and
            'OR' : lambda a, b: a | b,            #Bitwise or
            'XOR': lambda a, b: a ^ b,            #Bitwise xor
            'NOT': lambda a: ~a,                  #Bitwise not
        }

    def operate(self, op, op1 , op2):
        if op in self.alu_ops:
            return self.alu_ops[op](op1, op2)
        else:
            print("ERROR: Operation not found")
