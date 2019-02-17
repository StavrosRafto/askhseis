list1 = [1,2,6,-3,4,-2]
x = len(list1)
flag = 1

for i in range (x):
    S = []
    N = []
    s1 = list1[i]
    n1 = [list1[i]]
    
    for j in range (i+1,x):
        s1 = s1 + list1[j]
        S.append(s1)
        n1.append(list1[j])
        N.append(n1)

    if (flag == 1):
        maxs = S[0]
        maxn = N[0]
        flag = 0
        for k in range (1,len(S)):
            if (S[k] > maxs):
                maxs = S[k]
                maxn = N[k]       
    else:
        for k in range (len(S)):
            if (S[k] > maxs):
                maxs = S[k]
                maxn = N[k]

print (maxn)
print (maxs)
