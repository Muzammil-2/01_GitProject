import sys
a = int(input("Enter Your Age: "))
b = sys.argv[1]

def votingmc():
    if a >= 18 :
        print("you can vote")
    elif b == "congress":
        print("Indian")
        
    else:
        print("verfied before vote")
votingmc()
