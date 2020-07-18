def sum_fracts(a):
    if len(a)==0:
        return None
    else:
        b = 0
        l = [x[0] for x in a]
        l.sort(reverse = True)
        x = l[0]
        while  1:
            s = 0
            for i in l:
                if x%i == 0:
                    s+=1
            if s == len(l):
                break
            else:
                x+=1
        l1 = []
        for i in a:
            b = (x/i[1])*i[0]
            l1.append(b)
            b = 0
        deno = sum(l1)
        nemo = x
        final = [deno,nemo]
        
        if deno%nemo==0:
            return deno/nemo
        else:
            return final

print(sum_fracts([[1, 2], [1, 3], [1, 4]]))