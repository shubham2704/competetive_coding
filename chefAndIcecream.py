for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    
    c = l.count(15)
    counter = 0
    if l[0]>5:
        print("NO")

    elif c>=1:
        b = 0
        for i in l:
            ret = i-5
            if ret>0 and b<ret:
                print('NO')
                break
            if ret>0 and b>=ret:
                b+=5
                b-=ret
            if ret == 0 :
                b+=5 
            counter+=1
            
        if counter==len(l):
            print("YES")
        else:
            pass

    else:
        fi,te = 0,0
        for i in l:
            if i==5:
                fi+=1
            else:
                if fi>=1:
                    fi-=1
                    te+=1
                else:
                    print("NO")
                    break
            counter+=1

        if counter==len(l):
            print("YES")
        else:
            pass