with open("data.dat", "r") as f:
    countLines = 0
    for line in f:
        countZeros = 0
        countOnes = 0
        for char in line:
            if(char == '0'):
                countZeros += 1
            if(char == '1'):
                countOnes += 1
        if(countZeros % 3 == 0 or countOnes % 2 ==0):
            countLines += 1

print(countLines) ## flag
