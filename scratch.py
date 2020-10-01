l=[10, 1, 2, 3, 4, 5]
counter=0
for j in range(2):
    for i in range(len(l)):
        try:
            if l[i]<l[i-1]:
                counter+=1
                bad_egg=i
        except:
            pass
        try:
            if l[i]>l[i+1]:
                counter += 1
                bad_egg = i
        except:
            pass
        try:
            if l[i]==l[i-1] or l[i]==l[i+1]:
                counter+=1
                bad_egg = i
        except:
            pass


    l.remove(l[bad_egg])
if counter==1 or 0:
    print('Can be solved by emitting one number.')
else:
    print('impossible')


