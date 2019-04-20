import numpy as np
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

kosare = np.array([np.array(kosara) for kosara in kosare])
# print(kosare)
# exit(0)

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
        pretinci[(i * brPredmetaVelicina + j) % brPretinaca] += 1

for kosara in kosare:
    for (i, j) in combinations(kosara, 2):
        if pretinci[(i * brPredmetaVelicina + j) % brPretinaca] >= prag:
            parovi[str(i) + ' ' + str(j)] += 1

m = sum(1 for value in brPredmeta.values() if value >= prag)
sortirano = [par[1] for par in parovi.most_common() if par[1] >= prag]

print(m * (m-1) / 2)
print(len(sortirano))
for broj in sortirano:
    print(broj)

end = time.time()
sys.stderr.write(str(end - start))