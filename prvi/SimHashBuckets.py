import hashlib
import sys

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
    return str_sh


def diffBits(a, b): 
    n = a^b
    count = 0
    while n: 
        count += n & 1
        n >>= 1
    return count

def diffStr(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


def hash2int(pojas, simHash):
    stringHash = str(simHash)
    endIndex = 128 - 16 * pojas
    return int(stringHash[endIndex - 16 : endIndex], 2)

def removeDuplicates(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list



simHashes = []
querries = []
lineCount = 0
firstLine = True
N = 0

for idx, line in enumerate(sys.stdin):
    lineCount += 1

    if firstLine == True:
        N = int(line)
        firstLine = False
        continue

    if lineCount <= N+1:
        h = simhash(line)
        print(idx, h)
        simHashes.append(h)
        continue
    
    if lineCount == N+2:
        Q = int(line)
        continue
    
    querry = line.split()
    querries.append(querry)


kandidati = {}
brojPojasa = 8

for pojas in range(brojPojasa):
    pretinci = {}

    for trenutni_id in range(N):
        simHash = simHashes[trenutni_id]
        val = hash2int(pojas, simHash)

        tekstovi_u_pretincu = []
        if val in pretinci:
            tekstovi_u_pretincu = pretinci[val]

            for tekst_id in tekstovi_u_pretincu:
                if trenutni_id in kandidati:
                    kandidati[trenutni_id].append(tekst_id)
                else:
                    kandidati[trenutni_id] = [tekst_id]

                if tekst_id in kandidati:
                    kandidati[tekst_id].append(trenutni_id)
                else:
                    kandidati[tekst_id] = [trenutni_id]

        tekstovi_u_pretincu.append(trenutni_id)
        pretinci[val] = tekstovi_u_pretincu

for querry in querries:
    counter = 0
    I = int(querry[0])
    K = int(querry[1])
    if I not in kandidati:
        continue
    kandidatiBezDuplikata = removeDuplicates(kandidati[I])
    for kandidat in kandidatiBezDuplikata:
        if diffStr(simHashes[kandidat], simHashes[I]) <= K:
            counter += 1
    print(str(counter))
