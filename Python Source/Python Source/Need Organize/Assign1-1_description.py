#3개의 배열에서 3개의 요소(각각 배열에서)의 합이 목표 값과 같은지 확인하는 
#Python 프로그램을 작성하십시오. 
#3요소 조합을 모두 인쇄하십시오.
'''
샘플 데이터:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
목표 = 70
*/
'''
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

xmax = max(X)
ymax = max(Y)
zmax = max(Z)
xmin = min(X)
ymin = min(Y)
zmin = min(Z)

res = []

for x in X:
    if x + ymax + zmax < T or x + ymin + zmin > T: #T를 생성 못하는 경우 필터링
        continue
    for y in Y:
        if x + y + zmax < T or x + y + zmin > T:
            continue
        for z in Z:
            if x + y + z == T:
                res.append(str("[%d, %d, %d]" % (x, y, z)))
                
print(res)
