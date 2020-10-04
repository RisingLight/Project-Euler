from itertools import permutations 

def main(lst_digits,position=None):
    lst = []
    perms = permutations(lst_digits) 
    for permutation in perms:
        permutation = int("".join(map(str,permutation)))
        lst.append(permutation)
    lst.sort() # might be redundant
    if position:
        return str(lst[position-1]).zfill(len(lst_digits))
    else:
        for index,item in enumerate(lst):
            lst[index] = str(item).zfill(len(lst_digits))
        return lst


if __name__ == "__main__":
    print(main([0,1,2,3,4,5,6,7,8,9],1000000))