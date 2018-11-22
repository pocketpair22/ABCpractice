Sd = input()
T = input()
result = None
 
for i in range(len(Sd) - len(T), -1, -1):
    flag = True
    for j, k in zip(range(i, i+len(T)), T):
        if Sd[j] != k and Sd[j] != '?':
            flag = False
            break
 
    if flag:
        Sd_List = list(Sd)
        for j, k in zip(range(i, i+len(T)), T):
            Sd_List[j] = k
        Sd = "".join(Sd_List)
        result = Sd.replace('?', 'a')
        break
 
print(result if result else 'UNRESTORABLE')
