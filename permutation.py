def permutation(string):
    if len(string) == 0: 
        return []
    if len(string) == 1:
        return [string]
    
    lst = []
    for i in range(len(string)):
        first_char = string[i]
        remaining_string = string[0:i] + string[i+1:]

        for each in permutation(remaining_string):
            lst.append(first_char + each)
    lst.sort()

    return lst

with open("testcase.txt",'r') as file:
    for line in file: 
       print(",".join(permutation(line.rstrip('\n'))))
