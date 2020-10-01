l= [1, 3, 2, 1]
counter=0
bad_egg=None
for j in range(2):
    if  len(l)<=1:
        break
  
    if l[0]>=l[1]:
        counter += 1
        l.pop(0)
        continue

        
    elif l[len(l)-1]<=l[len(l)-2]:
        counter+=1
        l.pop(len(l)-1)
        continue
    
    for i in range(1,(len(l)-1)):
        
    
        if l[i]<l[i-1]:
            counter+=1
            bad_egg=i
            break
            
        elif l[i]>l[i+1]:
            counter += 1
            bad_egg = i
            break
    if bad_egg!=None:

        l.remove(l[bad_egg])
if counter==1 or 0:
    print('Can be solved by emitting one number.')
else:
    print('impossible')

