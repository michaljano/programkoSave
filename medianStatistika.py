import random
joj = []

POCET = 7
ROZSAH = 10
for i in range(POCET):
    joj.append(random.randint(0,ROZSAH))
print(joj)
print(sum(joj)/len(joj))
joj.sort()
if POCET%2 == 0:
    print(joj)
    print((joj[len(joj)//2]+joj[len(joj)//2-1])/2)
else:
    print(joj)
    print(joj[len(joj)//2])

