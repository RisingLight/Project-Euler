# Euler 22
def get_total_sum_of_names(names_file_path):
    name_file = open(names_file_path,"r")
    names = name_file.read()
    names = names.replace('\"','')
    names_list = names.split(",")
    names_list.sort()
    total_names_sum = 0
    for index,name in enumerate(names_list):
        name_sum = 0
        for ch in name:
            name_sum+=(ord(ch)-64)
        total_names_sum+=(name_sum*(index+1))

    return total_names_sum

if __name__ == "__main__":
    print(get_total_sum_of_names("p022_names.txt"))
