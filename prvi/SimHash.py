import hashlib
import sys
import time

def addZeroes(binaryString):
    length = len(binaryString)

    while(128 != length):
        binaryString = '0' + binaryString
        length += 1
    return binaryString

def simhash(text):
    sh = [0] * 128
    units = text.split()

    for unit in units:
        m = hashlib.md5()
        m.update(unit.encode('utf-8'))
        digest = m.hexdigest()
        bindigest = bin(int(digest, 16))[2:]
        bindigest = addZeroes(bindigest)

        for idx, bit in enumerate(bindigest):
            if int(bit) == 1:
                sh[idx] += 1
            else:
                sh[idx] -= 1

    for i in range(len(sh)):
        if int(sh[i]) >= 0:
            sh[i] = 1
        else:
            sh[i] = 0

    str_sh = ''.join(map(str, sh))
    return bin(int(str_sh, 2))
    
def diffBits(a, b): 
    n = a^b
    count = 0
    while n: 
        count += n & 1
        n >>= 1
    return count 

start = time.time()

firstLine = True
N = 0
Q = 0
simHashes = []
lineCount = 0

for line in sys.stdin:
    lineCount += 1

    if firstLine == True:
        N = int(line)
        firstLine = False
        continue

    if lineCount <= N+1:
        simHashes.append(simhash(line))
        continue
    
    if lineCount == N+2:
        Q = int(line)
        continue
    
    querry = line.split()
    I = int(querry[0])
    K = int(querry[1])
    counter = 0

    for idx, simHash in enumerate(simHashes):
        if idx == I:
            continue

        if diffBits(int(simHashes[I], 2), int(simHash, 2)) <= K:
            counter += 1

    print(str(counter))

end = time.time()
sys.stderr.write(str(end - start))