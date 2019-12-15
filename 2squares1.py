#Задача №2
N = int(input())
arr = list(map(int, input().split(maxsplit = N)))
arr = sorted(arr, key = lambda el: int(el))
t = arr[0]
res_arr = []
els = []
for el in arr:
	if el == t:
		els.append(el)
	else:
		res_arr.append(els)
		els = [el]
		t = el
res_arr.append(els)

cnt = 0;
for el in res_arr:
	cnt = cnt + len(el) // 4
print(cnt)
