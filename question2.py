import sys

def check_reverse(string1, string2):
    if string1[0:1] == string2[len(string2) - 1:len(string2)]:
        if len(string1) > 1:
            return check_reverse(string1[1:len(string1)], string2[0:len(string2)-1])
        else:
            return True
    else:
        return False

if len(sys.argv) != 3:
    print("Please call this function with 2 arguments")
    print("i.e. 'python question2.py string1 string2'")
elif len(sys.argv[1]) == len(sys.argv[2]):
    print(check_reverse(sys.argv[1], sys.argv[2]))
else:
    print("Strings not equal in length")
