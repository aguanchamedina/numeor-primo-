#input
n = int(input("Digite el numero: "))

#processing 
sw = 0 
for i in range(2, n-1):
    d = n%i
    if d==0:
       sw=1
if sw==0:
    print("ES NUMERO")
else:
    print("NO ES PRIMO")
    

 