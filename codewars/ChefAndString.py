t = int(input())
for _ in range(t):
    n = input()
    c=0
    counter = False


    for i in range(len(n)-1):
        if(counter == True):
            counter = False
            continue
        if n[i]=='x' and n[i+1]=='y' or n[i]=='y' and n[i+1]=='x':
            if i ==len(n):
                break
            else:
                c+=1
                counter = True

    print(c)