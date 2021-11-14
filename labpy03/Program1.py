x=100000000
sum=0
a=0 
lb=[int(0), int(0), int(x)*.1, int(x)*.1, int(x)*.5, int(x)*.5, int(x)*.5, int(x)*.2]
print("Modal awal pengusaha :", x )
for i in lb :
    sum=sum+i
    a+=1 
    print('laba bulan ke - ', a , 'sebesar:', i)

print('Total laba yang didapat adalah:', sum)