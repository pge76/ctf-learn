import binascii

# or simply linux: "strings minion.jpg | grep flag"

with open("minion.jpg", "rb") as f:
    byte_array = f.read(32)
    while(byte_array):
        print(byte_array.hex(), end="\t")
        for c in byte_array:
            if (c < 128 and c>31):
                print(chr(c), end="")
            else:
                print(" ", end="")
        print("", end="\n")
        byte_array = f.read(32)
