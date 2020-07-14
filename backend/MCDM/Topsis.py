import numpy as np
from numpy.core import cumsum, amax, amin
from numpy.ma import array, sqrt

# Entscheidungsmatrix X
# Kriterien: Preis (€/T), Co2 (Random Werte von 1-7), RW (siehe Mara), Gewicht (Fertigprodukt)
# verglichene Materialien bzw. Mara_id: 1 & 25
X = array([[750, 7, 0.73, 0.106],
           [890, 3, 0.84, 0.0408]])

# Gewichtungen der Kriterien w
w = array([0.25, 0.25, 0.25, 0.25])

# Schrit 1: Berechnung der normalisierten Entscheidungsmatrix NX
col_sums = array(cumsum(X**2, 0))
NX = array([[round(X[i, j] / sqrt(col_sums[X.shape[0]-1, j]), 4) for j in range(4)] for i in range(2)])
print('NX =', NX)

# Schritt 2: Berechnung der gewichteten normalisierten Entscheidungsmatrix V
V = array([[round(w[j] * NX[i, j], 4) for j in range(4)] for i in range(2)])
print ("V = ",V)

# Schrit 3: Bestimmung der idealen (A_stern) und anti-idealen Lösung (A_minus)
A_stern = array([amin(V[:, :1]), amax(V[:, 1:2]),amax(V[:, 2:3]), amin(V[:, 3:4])])
print ("A_stern = ",A_stern)

A_minus = array([amax(V[:, :1]), amin(V[:, 1:2]),amin(V[:, 2:3]), amax(V[:, 3:4])])
print ("A_minus = ",A_minus)

# Schrit 4: Berechnung der Trennungsmaße D_stern und D_minus
b1 = array([[(V[i, j] - A_stern[j])**2  for i in range(2)]for j in range(4)])
D_stern = np.round(sqrt(sum(b1, 0)),4)
print ('D_stern =',D_stern)

b2 = array([[(V[i, j] - A_minus[j])**2 for i in range(2)]for j in range(4)])
D_minus = np.round(sqrt(sum(b2, 0)),4)
print ('D_minus = ',D_minus)

# Schrit 5: Berechnung der relativen Nähe zur idealen Lösung
C_stern = array([round(D_minus[i] / (D_stern[i] + D_minus[i]),4) for i in range(2)])
print("C_stern = ", C_stern)