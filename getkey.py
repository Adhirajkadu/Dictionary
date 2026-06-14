tect_dict = {'Codingle' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print("The Original Dictonary :" + str(tect_dict))

K = 2

res = 0
for key in tect_dict:
    if tect_dict[key] == K:
        res = res + 1

print("Frequency of K is :" + str(res))