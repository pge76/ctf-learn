input1 = "0xc4115"
input2 = "0x4cf8"

binary1 = int(input1, 16)
binary2 = int(input2, 16)

result = binary1 ^ binary2

print('0x{:x}'.format(result))