A=int(input("Masukkan nilai A : "))
B=int(input("Masukkan nilai B : "))
C=int(input("Masukkan nilai C : "))

if A > B and B > C:
    print("Terbesar dari 3 buah bilangan ", A)
elif B > A and B > C:
    print("Terbesar dari 3 buah bilangan ", B)
else:
    print("Terbesar dari 3 buah bilangan ", C)
    