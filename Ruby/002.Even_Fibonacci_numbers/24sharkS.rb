# Euler Problem_02

a = 1
b = Math.sqrt(5)
phi0 = (a + b)/2
phi1 = (a - b)/2
i = 0
sum = 0
num = 0

while num.to_i <= 4000000
	if num.to_i%2 == 0
		sum+=num
	end
	i+=1
	num = ( phi0**i - phi1**i )/b
end

print sum.to_i
