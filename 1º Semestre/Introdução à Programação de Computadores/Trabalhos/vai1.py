n1 = int(input('1º número: '))
n2 = int(input('2º número: '))

cn1 = n1 // 100
dn1 = (n1 % 100) // 10 
un1 = n1 % 10

cn2 = n2 // 100
dn2 = (n2 % 100) // 10 
un2 = n2 % 10

vai1 = 0
if un1 + un2 >= 10:
    dn1 = dn1 + 1 
    vai1 = vai1 + 1  
if dn1 + dn2 >= 10:
    cn1 = cn1 + 1 
    vai1 = vai1 + 1       
if cn1 + cn2 >= 10:
    vai1 = vai1 + 1

print(f'{vai1} vai 1')


            
            

   
 