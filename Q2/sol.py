#Read data from input file
import sys
allValid = True
errorCodes = []
file = open("test.txt")
i = 0
for line in file:
    # first line, don't read
    if i != 0:
        # parse message in to list
       msg = line.rstrip().split()
       # if false
       if msg[1] == 'false':
           allValid = False
           errorCodes.append(msg[2])
    i += 1

if allValid:
    print("Yes")
else:
    print("No")
    for err_code in errorCodes:
        sys.stdout.write(f"{err_code} ")
    sys.stdout.write("\n")