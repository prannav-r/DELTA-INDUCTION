n=int(input("Enter the number of rows/columns: "))

for k in range(n-1):
    j = 0
    for i in range(n):
        print(' _ ', end = '')
        j += 1
        if j == n: break
        print('|', end = '')

    print()
        
for  a in range(n-1):
    print('   |', end = '')
