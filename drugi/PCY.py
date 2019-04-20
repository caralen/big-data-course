import math
import sys
from collections import Counter
from itertools import combinations
import time

lineCount = 0
brKosara = 0
brPretinaca = 0
prag = 0
kosare = []

start = time.time()

for line in sys.stdin:
    lineCount += 1

    if lineCount == 1:
        brKosara = int(line)
    elif lineCount == 2:
        prag = math.floor(float(line) * brKosara)
    elif lineCount == 3:
        brPretinaca = int(line)
    else:
        kosare.append(map(int, line.split()))


brPredmeta = Counter()
pretinci = Counter()
parovi = Counter()

for kosara in kosare:
    for predmet in kosara:
        brPredmeta[predmet] += 1

brPredmetaVelicina = sum(brPredmeta.values())

for kosara in kosare:
    for predmet in kosara:
        if brPredmeta[predmet] < prag:
            kosara.remove(predmet)


for kosara in kosare:
    for (i, j) in combinations(kosara, 2):
        parovi[i, j] += 1

m = sum(1 for value in brPredmeta.values() if value >= prag)
sortirano = [par[1] for par in parovi.most_common() if par[1] >= prag]

file = open('moj.out', 'w+')

file.write('%s\n' % str(m * (m-1) / 2))
file.write('%s\n' % str(len(sortirano)))
for broj in sortirano:
    file.write('%s\n' % str(broj))

end = time.time()
sys.stderr.write(str(end - start))