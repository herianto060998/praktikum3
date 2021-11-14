print ("menampilkan bilangan terbesar dari n buah data yang diinputkan.")

max = 0

while True :

    a=int(input("masukkan nilai :"))

    if max < a :
        max = a
    
    if a==0 :
         break 

print("Bilangan terbesar adalah = ", max)