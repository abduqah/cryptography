def to_int(char):
    if(ord(char)-ord('0')<=9):
        return char
    else :
        return ord(char)-ord('A')+10


print(to_int('A'))