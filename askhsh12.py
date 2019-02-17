Text1 = input("Γράψε ένα κείμενο: ")
Text = list(Text1)
x = len(Text)

K = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
P = "αβγδεζηθικλομνοπρστυφχψω"
KG = list(K)
PG = list(P)
T = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Ειχα σκεφτει πολυ πιο γρηγορο τροπο αλλα παρουσιαζε προβλημα
for i in range(x):
    if (Text[i] == "α" or Text[i] == "Α"):
        T[0] = T[0] + 1

    elif (Text[i] == "β" or Text[i] == "Β"):
        T[1] = T[1] + 1

    elif (Text[i] == "γ" or Text[i] == "Γ"):
        T[2] = T[2] + 1
        
    elif (Text[i] == "δ" or Text[i] == "Δ"):
        T[3] = T[3] + 1
        
    elif (Text[i] == "ε" or Text[i] == "Ε"):
        T[4] = T[4] + 1

    elif (Text[i] == "ζ" or Text[i] == "Ζ"):
        T[5] = T[5] + 1        

    elif (Text[i] == "η" or Text[i] == "Η"):
        T[6] = T[6] + 1

    elif (Text[i] == "θ" or Text[i] == "Θ"):
        T[7] = T[7] + 1

    elif (Text[i] == "ι" or Text[i] == "Ι"):
        T[8] = T[8] + 1

    elif (Text[i] == "κ" or Text[i] == "Κ"):
        T[9] = T[9] + 1

    elif (Text[i] == "λ" or Text[i] == "Λ"):
        T[10] = T[10] + 1
    
    elif (Text[i] == "μ" or Text[i] == "Μ"):
        T[11] = T[11] + 1

    elif (Text[i] == "ν" or Text[i] == "Ν"):
        T[12] = T[12] + 1

    elif (Text[i] == "ξ" or Text[i] == "Ξ"):
        T[13] = T[13] + 1

    elif (Text[i] == "ο" or Text[i] == "Ο"):
        T[14] = T[14] + 1

    elif (Text[i] == "π" or Text[i] == "Π"):
        T[15] = T[15] + 1

    elif (Text[i] == "ρ" or Text[i] == "Ρ"):
        T[16] = T[16] + 1

    elif (Text[i] == "σ" or Text[i] == "Σ"):
        T[17] = T[17] + 1
        
    elif (Text[i] == "τ" or Text[i] == "Τ"):
        T[18] = T[18] + 1

    elif (Text[i] == "υ" or Text[i] == "Υ"):
        T[19] = T[19] + 1

    elif (Text[i] == "φ" or Text[i] == "Φ"):
        T[20] = T[20] + 1

    elif (Text[i] == "χ" or Text[i] == "Χ"):
        T[21] = T[21] + 1

    elif (Text[i] == "ψ" or Text[i] == "Ψ"):
        T[22] = T[22] + 1

    elif (Text[i] == "ω" or Text[i] == "Ω"):
        T[23] = T[23] + 1

for i in range(24):
    if (T[i] != 0):
        mint = T[i]
        minp = i
        maxt = T[i]
        maxp = i
        break

for i in range(24):
    if (T[i] != 0):
        if (T[i] > maxt):
            maxt = T[i]
            maxp = i
        elif (T[i] < mint):
            mint = T[i]
            minp = i

for i in range(x):
    if (Text[i] == KG[maxp] or Text[i] == PG[maxp]):
        Text[i] = KG[minp]
    elif (Text[i] == KG[minp] or Text[i] == PG[minp]):
        Text[i] = KG[maxp]

T1 = "".join(Text)
print (T1)




