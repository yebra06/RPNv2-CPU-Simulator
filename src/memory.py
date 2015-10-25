from collections import deque
from i_o import io
import sys

class Memory:
    def __init__(self):
        """Standard memory unit inside a computer with methods to load file data and access/operate stack."""
        self.RAM = []               #Random access memory
        self.STACK = deque([])      #Stack of data using LIFO
        self.SP = 0                 #Stack pointer points to top of stack

    def loader(self, cfile):
        """Process and store file data and load it into RAM."""
        try:
            for i in open(cfile, 'r+').read().splitlines():
                print(i)
                self.RAM.append(i)
            return len(self.RAM)
        except:
            print(cfile + " not found. System terminating...")
            sys.exit()

    def read(self, addr):
        """Retrieve address from PC register and return data at specified address."""
        if addr < len(self.RAM):
            return self.RAM[addr]

    def push(self, data):
        """Push retrieved data onto stack and point SP register to top of stack."""
        self.STACK.appendleft(data)
        self.SP = self.STACK[0]

    def pop(self):
        """Pop data off of stack."""
        op1 = self.STACK.popleft()
        op2 = self.STACK.popleft()
        return op1, op2
