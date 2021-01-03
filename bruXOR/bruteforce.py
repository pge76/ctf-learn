input = "q{vpln'bH_varHuebcrqxetrHOXEj"
crib = "flag"

def xor(s, key):
    return ''.join(chr(ord(x) ^ key) for(x) in s)

result = list([xor(input, i) for i in range(255)])
print(list(filter(lambda x: x.startswith(crib), result))[0])



