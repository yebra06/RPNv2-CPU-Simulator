import time
import sys

from i_o import io
from alu import ALU
from memory import Memory

class Controller:
    def __init__(self):
        """Model of a standard contoller unit demonstrating the Texas 4-step (fetch,decode,execute,store) with methods for each."""
        self.R1 = 0                 #General purpose register to store final result.
        self.R2 = 0                 #General purpose register to store file length.
        self.R3 = ""                #Storage register to store mnemonic from memory.
        self.IR = 0                 #Instruction register
        self.PC = 0                 #Program counter/accumulator
        self.running = False        #Machine state
        self.clock = time.time()    #Start system clock
        self.ALU = ALU()            #Arithmetic-logic units
        self.MEM = Memory()         #System memory

    def loader(self, cfile):
        """Load file data into memory prior 4-step and store it into gp register R2."""
        io("Loading " + cfile + "...")
        self.R2 = self.MEM.loader(cfile)
        io("Processed: " + str(self.R2) + " lines.")
        io("Machine is running...")
        self.running = True

    def fetch(self):
        """Fetch next instruction stored in memory using PC address and store it into storage register R3."""
        self.R3 = self.MEM.read(self.PC)
        io("|FETCH|--> address(" + str(self.PC) + ")")
        io(">read(" +str(self.PC)+ "->" + self.R3 + ")")

    def decode(self):
        """Decode data fetched. Determine if valid value or instruction, bump accumulator, and store in inst register IR."""
        self.PC += 1
        try:
            self.IR = int(self.R3)
            self.R3 = "push"
            io("\t|DECODE|--> decoding(" + str(self.IR) + ")...")
            io("\t>found operand(" + str(self.IR) + ")")
            io("\t>valid instruction")
        except ValueError:
            self.IR = self.R3
            io("\t|DECODE|--> decoding(" + self.IR + ")...")
            io("\t>found operator(" + self.IR + ")")
            io("\t>valid instruction")

    def execute(self):
        """Execute instruction fetched from memory and operate/manage stack memory."""
        op = self.R3
        if op == "push":
            io("\t\t|EXECUTE|--> " + op)
            io("\t\t>pushed(" + str(self.IR) + ")")
            self.MEM.push(self.IR)
        else:
           op1, op2 = self.MEM.pop()
           io("\t\t|EXECUTE|--> " + op + "(" + str(op1) + "," + str(op2) + ")")
           io("\t\t>pop  <-(" + str(op1) + ")")
           io("\t\t>pop  <-(" + str(op2) + ")")
           self.R1 = self.ALU.operate(op, op1, op2)
           io("\t\t>push ->(" + str(self.R1) + ")")
           self.MEM.push(self.R1)

    def store(self):
        """Store resulting data, output value that is stored in register."""
        io("\t\t\t|STORE|--> storing(" + str(self.R1) + ")")

    def run(self):
        """Start steppin. Begin the Texas 4-step, calculate/display the total processing time, and display final result."""
        while self.running and self.PC < self.R2:
            io('=' * 62)
            self.fetch()
            self.decode()
            self.execute()
            self.store()
        io('='*62 + "\nResult:\t" + str(self.R1) + "\nTime  :\t"
            + str(round(time.time() - self.clock, 4)) + " s\n" +'='*62)

