frase = "Hola, mi nombre es Linder. Mi nombre completo es linder linder(linder3hs)"
arrayPalabras=[]
word=""
for i in frase:
    word=word+i
    if i==',' or i=='.' or i=='(' or i==')' or i==" ":
        #arrayPalabras.add({"${word}":""})
        #word[1:-2]
        if(word[:-1]==""):
            continue
        arrayPalabras.append(word[:-1])
        word=""
        continue

print(arrayPalabras)

x = arrayPalabras.count('nombre')
print(x)

arrayFinal=[]
for i in arrayPalabras:
    x=arrayPalabras.count(i)
    arrayFinal.append({i:x})

print(arrayFinal)