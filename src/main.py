from machine import Machine

def main():
    print('\n' +'-'*22 + "RPN Calculator v0.2" + '-'*21)
    cfile = "rpn_file.txt"
    Machine(cfile)

if __name__ == "__main__":
    main()
