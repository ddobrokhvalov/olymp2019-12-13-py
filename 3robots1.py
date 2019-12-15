#Задача №3
def distance2(c1, c2):
	return ((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)**0.5
	
orts = {'L':[-1,0], 'R':[1,0], 'U':[0,1], 'D':[0,-1], 'I':[0,0]}
c1 = list(map(int, input().split(maxsplit = 2)))
c2 = list(map(int, input().split(maxsplit = 2)))
commands = str(input())
res_com1 = []
res_com2 = []
for i in range(len(commands)):
	c1n = [c1[0] + orts[str(commands[i])][0], c1[1] + orts[str(commands[i])][1]]
	c2n = [c2[0] + orts[str(commands[i])][0], c2[1] + orts[str(commands[i])][1]]
	if distance2(c1n, c2) > distance2(c1, c2):
		res_com1.append('I')
	elif distance2(c1n, c2n) > distance2(c1, c2):
		res_com1.append('I')
	else:
		res_com1.append(commands[i])
		c1 = c1n
		
	if distance2(c2n, c1) > distance2(c2, c1):
		res_com2.append('I')
	elif distance2(c2n, c1n) > distance2(c2, c1):
		res_com2.append('I')
	else:
		res_com2.append(commands[i])
		c2 = c2n
	if distance2(c1,c2) == 0:
		break
if distance2(c1,c2) == 0:
	print('YES')
	print("".join(res_com1))
	print("".join(res_com2))
else:
	print('NO')
