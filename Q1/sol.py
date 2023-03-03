import os
import sys
import functools

# custom comparator
#return true if a <= b
def my_comp(a, b):
    hard_code = {'S': 0, 'M': 1, 'L': 2}
    if a == b:
        return 0

    if a[-1] != b[-1]:
        return -1 if hard_code[a[-1]] < hard_code[b[-1]] else 1
    elif a[-1] == 'L':
        # more x is larger
        return -1 if len(a) < len(b) else 1
    elif a[-1] == 'S':
        # less X is larger
        return -1 if len(a) > len(b) else 1

# return index of that shirt that satisfied, otherwise return -1
def find_index(tShirts, request_shirt):
    i = 0
    for shirt in tShirts:
        if my_comp(request_shirt,shirt):
            # if one larger or equal shirt found
            # print(request_shirt,"use ", tShirts[i])
            return i
        i += 1
    
    return -1

def solution():
    filename = "test.txt"
    total_shirts = 0
    total_request = 0
    requests = []
    tShirts = []

    # function to parse file
    def parse_file(filename):
        file = open(filename)
        i = 0
        nonlocal total_shirts
        nonlocal total_request
        nonlocal requests
        nonlocal tShirts 
        for line in file:
            line = line.rstrip()
            if i == 0:
                total_shirts = int(line.strip())
            elif i == 1:
                tShirts = line.split()
            elif i == 2:
                total_request = int(line.strip())
            elif i == 3:
                requests = line.split()
            else:
                break
            i += 1
    # call function
    parse_file(filename)
    # sort the tShirts in ascending order
    sorted_tShirts = sorted(tShirts, key=functools.cmp_to_key(my_comp))
    sorted_requests = sorted(requests, key=functools.cmp_to_key(my_comp))
   

    # check size:
    if total_request > total_shirts:
        print("No")
    
    # loop through
    for shirt in sorted_requests:
        index = find_index(sorted_tShirts,shirt)
        
        if index != -1:
            # if the tShirts found
            del sorted_tShirts[index]
        else:
            # no satisfied found
            print("No")
            return

    print("Yes")

    
    
solution()