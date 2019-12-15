#Задача №1
N = int(input())
k = int(input())
N2 = N//100
ret = 100 * N2
for i in range(99, -1, -1):
	if (100 * N2 + i) % k == 0:
		ret = 100 * N2 + i
print(ret)
