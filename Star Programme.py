B = int(input("Enter any one number out of 1 and 0 "))
Boolean = bool(B)
n = int(input("Enter number of rows "))
if Boolean == True:
    for i in range(0,n+1):
        j = i
        while j>0:
            print("* ", end = '')
            j = j-1
        print("\n")
if Boolean == False:
    i = n
    while i >0:
        for j in range(0,i):
            print("* ",end = '')
        print("\n")
        i = i-1
