import string
import numpy

input = "gwox{RgqssihYspOntqpxs}"
key = "blorpy"

alphabet = list(string.ascii_lowercase)

fail = 0
output = ""

for i in range(0, len(input)):
    if(input[i] in alphabet):
        c = key[(i - fail) % len(key)]
        #print(c)
        keyIndex = alphabet.index(c)
        msgIndex = alphabet.index(input[i])
        output += alphabet[(msgIndex - keyIndex + len(alphabet)) % 26];
    elif(input[i].lower() in alphabet):
        c = key[(i - fail) % len(key)].lower()
        # print(c)
        keyIndex = alphabet.index(c)
        msgIndex = alphabet.index(input[i].lower())
        output += alphabet[(msgIndex - keyIndex + len(alphabet)) % 26].upper();
    else:
        output += input[i]
        fail+=1

print(output)
