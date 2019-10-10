# Euler 01. Multiples of 3 and 5
count=0
for(number in 1:999){
  if(number%%3==0 || number%%5==0){
    count=count+number
  }
}
print(count)
