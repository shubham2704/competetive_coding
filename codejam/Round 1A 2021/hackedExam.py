for t in range(int(input())):
    n,q = map(int,input().split())
    ans = []
    score = []
    for _ in range(n):
        a,s = map(str,input().split())
        ans.append(a)
        score.append(s)
        
    if n == 1:
        print(f'case #{t+1}: {a} {s}/{1}') 
    else:
        m = score.index(max(score))
        # score1 = score[:m] + score[m+1:]
        for x in score:
            c = 0
            if x==max(score):
                c+=1
                if c==2:
                    m1 = score.index(x)
                    s1 = ans[m]
                    s2 = ans[m1]
                    
        print(f'case #{t+1}: {ans[m]} {score[m]}/1')

'''
4
1 3
FFT 3
1 3
FFT 2
2 6
FFTTTF 2
FTFTFT 4
2 2
FF 1
TT 1
'''
