for i in range (5):
    print(i)

print("While")
sayaç = 5 
while sayaç!=0:
    print(sayaç)
    sayaç -=1


print(" ")
print("Arabalar: ")
arabalar =["mercedes","Bmv","Porche"]
for i in arabalar :
    print(i)
print(" ")
print("Meyveler: ")
meyveler =["elma","portakal","kavun"]
for i ,meyve in enumerate(meyveler):
    print(i,meyve)


print("Zip")
isimler =["Ali","Veli"]    
yaşlar=[23,25]
for isim,yas in zip(isimler,yaşlar):
    print(isim,yas)
    
print(" ")
print("List Comprehension")
kareler =[x**2 for x in range(5)]
print(kareler)    