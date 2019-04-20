from __future__ import division
from decimal import Decimal, ROUND_HALF_UP
import numpy as np
from scipy import spatial
import sys

def transformMatrix(matrix):
    N, M = np.shape(matrix)
    transformed = np.empty([M,N])

    for i in range(int(M)):
        a = np.copy(matrix[i,:])
        mean = np.sum(a) / np.count_nonzero(a)
        a[a != 0] -= mean
        transformed[i,:] = a
    return transformed

def calculateRecomendation(retci, trans, i, j, N, M, K):
    slicnosti = 1 - spatial.distance.cdist(trans, np.array([trans[i,:]]), 'cosine')
    sortIndex = np.argsort(-np.reshape(slicnosti, -1))

    stupac = np.reshape(retci[:,j], -1)[sortIndex]
    slicni = np.reshape(slicnosti, -1)[sortIndex]

    nijeX = stupac != 0
    stupac = stupac[nijeX]
    slicni = slicni[nijeX]

    neNegativni = slicni > 0
    stupac = stupac[neNegativni][:K]
    slicni = slicni[neNegativni][:K]
    
    return np.dot(stupac, slicni) / np.sum(slicni)

lineCounter = 0
N = M = Q = 0
I = J = T = K = 0

upiti = []
retci = []

for line in sys.stdin:
    lineCounter += 1
    lajna = [0 if el == 'X' else float(el) for el in line.split()]

    if lineCounter == 1:
        N, M = map(int, lajna)
    elif lineCounter == M + 2:
        Q = lajna[0]
    elif lineCounter > M + 2:
        upiti.append(map(int, lajna))
    elif lineCounter == 2:
        retci = np.array(lajna)
    else:
        retci = np.vstack((retci, np.array(lajna)))

for upit in upiti:
    I, J, T, K = upit
    rezultat = 0

    if T == 0:
        rezultat = calculateRecomendation(retci, transformMatrix(retci), I-1, J-1, N, M, K)
    else:
        rezultat = calculateRecomendation(retci.T, transformMatrix(retci.T), J-1, I-1, N, M, K)

    print(Decimal(Decimal(rezultat).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)))
