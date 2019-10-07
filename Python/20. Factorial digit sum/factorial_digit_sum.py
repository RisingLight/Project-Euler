def fact(n, mem={0:1, 1:1):
    try:
        return mem[n]
    except KeyError:
        mem[n] = n * fact(n-1)
        return mem[n]

def fact_digit_sum(n):
    fact_digit = fact(n)
    fact_digit_list = [int(i) for i in str(fact_digit)]
    return sum(fact_digit_list)
    

print(fact_digit_sum(100))
