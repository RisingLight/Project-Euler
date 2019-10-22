# Euler Problem_01

i=3
sum=0
while i<1000
	if (i%3==0) or (i%5==0)
		sum+=i
	end
	i+=1
end

puts sum
