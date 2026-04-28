from typing import List

def read_integers() -> List[int]:
    string = input()
    string_list = list(string.split(","))
    for i in range(len(string_list)):
        string_list[i] = int(string_list[i])
    return string_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
