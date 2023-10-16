from math import sqrt

nbSegment = 1000000
Vinit = 0
t = 0

for i in range(1,nbSegment + 1):

    Xk = (i - 1) * (5 / nbSegment)
    Xk1 = i * (5 / nbSegment)

    Yk = ( (2*17)/3 - sqrt(((2*17)/3)**2-4*(Xk**2-10*Xk+25)) ) / 2
    Yk1 = ( (2*17)/3 - sqrt(((2*17)/3)**2-4*(Xk1**2-10*Xk1+25)) ) / 2

    det = (Yk - Yk1) / (Xk1 - Xk)
    racine = sqrt((Yk - Yk1)**2 + (Xk1 - Xk)**2)

    denom = (9.81*det) / (sqrt(det**2+1))
    numer = -Vinit + sqrt(Vinit**2 + 2*denom * racine)

    t = t + (numer / denom)

    # Determiner la nouvelle vitesse intitiale
    Vinit = sqrt(2*(29.43417 - 9.81 * Yk1))   
    
print(t)