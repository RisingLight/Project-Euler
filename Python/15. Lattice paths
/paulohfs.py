#Euler Problem_15
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

print(int((fatorial(2*20))/(fatorial(20)*fatorial(20))))
