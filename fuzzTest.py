import random

def fuzzer(max_len: int = 100, char_start: int = 65, char_range: int =26) -> str:
    #string_len = random.randrange(0,max_len)
    string_len = max_len
    out = ""
    for i in range(0,string_len):
        out += chr(random.randrange(char_start,char_start+char_range))

    #print(out)
    return out

#fuzzer(100,32,95)
