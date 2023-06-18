import sys
import compute

if __name__=="__main__":
    args = sys.argv[1::]
    if len(args) == 1 and compute.parsing(args[0].split()) == 0:
        compute.solve(args[0])
    exit()