zadachi = int(input())
n = 0

for i in range(zadachi):
    opinions_str = input() #"1 1 0" 
    opinions_splited = opinions_str.split() #["1", "1", "0"]
    sum_opinions = 0
    for a in opinions_splited:
        sum_opinions += int(a)
    if sum_opinions >= 2:
        n += 1   
print(n)