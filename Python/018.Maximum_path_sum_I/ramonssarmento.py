#Euler Problem_18

def calc(l,index,line):
	if line >= len(l) or index > line or index < 0:
		return 0
	value = int(l[line].split()[index])
	left = value + calc(l,index,line+1)
	right = value + calc(l,index+1,line+1)
	return left if left > right else right




inputs = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

lines = inputs.split("\n")
print(calc(lines,0,0))
#best path: 75 + 64 + 82 + 87 + 82 + 75 + 73 + 28 + 83 + 32 + 91 + 78 + 58 + 73 + 93 = 1074
