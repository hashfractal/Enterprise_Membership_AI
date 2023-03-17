#EPTGMK

n = int(input())

K = n // 1000 % 1000
M = n // 1000000 % 1000
G = n // 1000000000 % 1000
T = n // 1000000000000 % 1000
P = n // 1000000000000000 % 1000
E = n // 1000000000000000000 % 1000

resK = ""
resM = ""
resG = ""
resT = ""
resP = ""
resE = ""

if K > 0:
    resK = str("%dK" % K)
if M > 0:
    resM = str("%dM" % M)
if G > 0:
    resG = str("%dG" % G)
if T > 0:
    resT = str("%dT" % T)
if P > 0:
    resP = str("%dP" % P)
if E > 0:
    resE = str("%dE" % E)

result = resE + resP + resT + resG + resM + resK

print(result)