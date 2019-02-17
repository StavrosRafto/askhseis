def function(list1,x,max2,first,last):
    for i in range(last,first,-1):
        
        if ((list1[i] + max2) <= x):
            max2 += list1[i]
            function(list1,x,max2,first,i-1)
            
    return (max2)

def maxDistance(list1,x):
    list1.sort()
    max1 = 0
    max2 = 0
    
    if (sum(list1) < x):
        return sum(list1)
    
    L = len(list1)
    for first in range(L):
        max2 = list1[first]
        for last in range(L-1,first,-1):
            
            if ((list1[last] + max2) <= x):
                max2 = function(list1,x,max2,first,last)
                max1 = max(max2,max1)
                
    return (max1)

list1 = []
n = 1
while (n != 0):
    n = int(input("Δώσε απόσταση (δώσε μηδέν (0) για να σταματήσεις): "))
    if (n < 0):
        print ("Δώσε θετικό αριθμό")
    elif (n > 0):
        list1.append(n)
        

x = int(input ("Δώσε έναν θετικό ακέραιο: "))

while (x <= 0):
    x = int (input("Παρακαλώ δώστε ΘΕΤΙΚΟ ακέραιο: "))



print("Το μέγιστο μικρότερο άθροισμα από το θετικό ακέραιο είναι: ",maxDistance(list1,x))
