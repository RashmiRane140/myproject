
Space=4
for i in range(1,6):
    for j in range(Space,0,-1):
      print(end=' ')
    for j in range(1,i+1):
        print("*",end=' ')
    Space-=1
    print()
print( )

for i in range(1,6):
    for j in range(5,0,1):
        print("",end=" ")
        for k in range(1,i+1):
            print("*",end=" ")
    print( )


