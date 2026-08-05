#Task 1-->workout with all possibilites of scling and striding
city='metropolitancity' #m-0,e-1,t-2,r-3,o-4,p-5,o-6,l-7,i-8,t-9,a-10,n-11,c-12,i-13,t-14,y-15
print(city[:4])
print(city[4:])
print(city[-6:-3])
print(city[-6:])
print(city[:-7])
print(city[5:8])
print(city[2:-7])
print(city[-1:7])



#Task 2 --> use loops and stings to print A to Z in same line
for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end=' ')
