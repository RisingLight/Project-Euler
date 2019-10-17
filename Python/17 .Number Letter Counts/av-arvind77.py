#EULER PROBLEM 17
import time

#time at the start of execution
start = time.time()

#dictionary to store the values
dic = {n:0 for n in range(0,1001)}

#intial values given manually
dic[0] = 0

dic[1] = 3

dic[2] = 3

dic[3] = 5

dic[4] = 4

dic[5] = 4

dic[6] = 3

dic[7] = 5

dic[8] = 5

dic[9] = 4

dic[10] = 3

dic[11] = 6

dic[12] = 6

dic[13] = 8

dic[14] = 8

dic[15] = 7

dic[16] = 7

dic[17] = 9

dic[18] = 8

dic[19] = 8

dic[20] = 6

dic[30] = 6

dic[40] = 5

dic[50] = 5

dic[60] = 5

dic[70] = 7

dic[80] = 6

dic[90] = 6

for i in range(21,100):
	tens = int(i/10)*10
	ones = i - tens
	dic[i]  = dic[tens]+dic[ones]
for i in range(100,1000):
	hundreds = int(i/100)
	tens_ones = i - hundreds*100
	if tens_ones == 0:
		dic[i] = dic[hundreds] + 7
	else:
		dic[i] = dic[hundreds] +10+dic[tens_ones]
dic[1000] = 11
print(sum(dic.values()))
end = time.time()
print(end-start)