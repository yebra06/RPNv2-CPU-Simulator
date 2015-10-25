#Programmer: Alfredo Yebra
#Date:       October 3, 2015

from controller import Controller
class Machine:
    def __init__(self, cfile):
        """This Machine class sends a codefile to be processed and loaded into memory then starts running the 4-step process."""
        self.c = Controller()       #Call controller
        self.c.loader(cfile)        #Send file to be loaded
        self.c.run()                #Run program
