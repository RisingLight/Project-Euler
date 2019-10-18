# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:26:19 2019

@author: Prajwal
"""
numbers=[i for i in range(1, 1001)]
ones={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens={1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
tens_ones={11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
spellings=[]
for i in range(len(numbers)):
    numbers[i]=str(numbers[i])
for i in range(len(numbers)):
    #if(i.len()==1):
    if(len(numbers[i])==1):
        spellings.append(ones[int(numbers[i])])
        
        

        
        
    elif(len(numbers[i])==2):
        if(numbers[i][1]=='0'):
            spellings.append(tens[int(numbers[i][0])])
        else:
            if(int(numbers[i]) in tens_ones.keys()):
                spellings.append(tens_ones[int(numbers[i])])
            else:
                n=int(numbers[i])
                tenth=int(n/10);
                units=n%10;
                string=tens[tenth]+ones[units]
                spellings.append(string)
            
            
            

        
    elif((len(numbers[i])==3)):
        if((numbers[i][2]=='0') and (numbers[i][1]=='0')):
            string=ones[int(numbers[i][0])]+'hundred'
            spellings.append(string)
        else:
            n=int(numbers[i])
            hundredth=int(n/100)
            tenth=int((n/10)%10)
            units=(n%100)%10
            string=ones[hundredth]+'hundred'+'and'
            if(int(numbers[i][1:]) in tens_ones.keys()):
                string+=tens_ones[int(numbers[i][1:])]
            elif(int(numbers[i][1])==0):
                string+=ones[int(numbers[i][2])]
            elif(numbers[i][2]=='0'):
                string+=tens[int(numbers[i][1])]
            else:
                string+=tens[tenth]+ones[units]
            spellings.append(string)

spellings.append('onethousand')    

str_len=0
for i in range(len(spellings)):
    str_len+=len(spellings[i])
print("Total letters used : ", str_len)



#print(numbers)
