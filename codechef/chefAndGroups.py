# for _ in range(int(input())):
#     s = input()
#     print(len(' '.join(s.split('0')).split()))

# i = 0
# s = []
# l = [7,6,5,4,3,2,1]
# print(l.index(min(l)))
# l1 = l[i:l.index(min(l))+1]
# j = l1.index(min(l1))
# s.append(l[j])
# s.append(l[i])
# print(s)
# j = 0
# c1 = []
# for i in range(6):
#     c = i+j
#     c1.append(c)
#     j+=1
#     print(f'{i} + {j} = {c}')
# print(c1)
# print(sum(c1))

# s = ''
# x,y,st = s[0], s[1], [x for x in s[2] ]
# print(s)
# print(st)
# st = ['c','j','?','c','c','?']
# cj = "".join(['cj']*len(st))
# print(cj)
# st.pop(st.index('?'))
# st.pop(st.index('?'))
# print(st)
# n = 7
# l = list(range(1,n+1))
# print(l)

# n,p = input().split()
# print(n,p)
n = 7
l = [str(x) for x in range(1,n+1)]
print(l)
"""
Moon And Umbrellas

def moon(p,a,b):
    fee = 0
    fee =p.count("CJ")*a + p.count("JC")*b
    return fee
def solve():
    t= input().split()
    a = int(inp[0])
    b = int(inp[1])
    p = t[2]
    fee = moon(p,a,b)
    length = len(p)
    i = 0
    while i < length:
        m =""
        if i > 0 and p[i] == "?":
            m = p[i-1]
        while p[i] == "?":
            if i < (length-1):
                i = i+1

            else:
                break

        f = m + p[i]
        if f == "CJ":
                fee += a
        elif f == "JC":
                fee += b
        i+=1

    print("Case #"+str(u+1)+": "+ str(fee))

for u in range(int(input())):
    solve()
"""

"""
RevrseSort Engineering

import math
from itertools import permutations


class permute:
    n = 0
    count = 0
    def __init__(self, n):
        self.n = n
    def next(self):
        a = []
        num = self.count
        for i in range(self.n-1, 0, -1):
            f = math.factorial(i)
            c = math.floor(num / f)
            a.append(c+1)
            num = num - c*f
        self.count = self.count+1
        a.append(1)
        return self.fill(a)
    def fill(self, a):
        p = [0]*self.n
        v = self.n
        for i in range(0, len(a)):
            zeroes = 0
            for j in range(0, len(p)):
                if p[j] == 0:
                    zeroes +=1
                if zeroes == a[i]:
                    p[j] = v
                    v -= 1
                    break
        return p



def genlist(l,n1,c1):
    n2 = math.factorial(n1)
    p = permute(n1)
    for o in range(n2):
        ln = p.next()
        lnc = ln[0:]
        c = 0
        for i in range(n1-1):
            #print(ln)
            j = ln.index(min(ln[i:n1+1]))
            ln[i:j + 1] = reversed(ln[i:j + 1])
            #print(j)
            #print(i)
            c += (j)-(i)+1
            #print(c)
        #print(c)
        if c1 == c:
            return lnc
    return -1

n = int(input())
lf = []
for k in range(n):
    l = input()
    l = l.split()
    n1 = int(l[0])
    c1 = int(l[1])
    #print(n1)
    l = []
    for i in range(1,n1+1):
        l.append(i)
    #print(l)
    ln = genlist(l,n1,c1)
    if ln == -1:
        lf.append('IMPOSSIBLE')
    else:
        s = [str(i) for i in ln]
        st = " ".join(s)
        lf.append(st)
for i in range(n):
    print('Case #'+str(i+1)+": "+lf[i])

    
    
#Alternate
'''from itertools import permutations
def genlist(l,n1,c1):
    perm = permutations(l)
    for l1 in list(perm):
        ln = list(l1)
        lnc = list(l1)
        c = 0
        for i in range(n1-1):
            #print(ln)
            j = ln.index(min(ln[i:n1+1]))
            ln[i:j + 1] = reversed(ln[i:j + 1])
            #print(j)
            #print(i)
            c += (j)-(i)+1
            #print(c)
        #print(c)
        if c1 == c:
            return lnc
    return -1
n = int(input())
lf = []
for k in range(n):
    l = input()
    l = l.split()
    n1 = int(l[0])
    c1 = int(l[1])
    #print(n1)
    l = []
    for i in range(1,n1+1):
        l.append(i)
    #print(l)
    ln = genlist(l,n1,c1)
    if ln == -1:
        lf.append('IMPOSSIBLE')
    else:
        s = [str(i) for i in ln]
        st = " ".join(s)
        lf.append(st)
for i in range(n):
    print('Case #'+str(i+1)+": "+lf[i])
'''
"""

"""
ReverSort ENgineering

def createL(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    return l 

def operationL(n, p):
    if p < n-1:
        return []
    l = []
    t = 0 
    c = 1
    for i in range(n-1, 0, -1):
        c += 1

        if t+c+i-1 >= p:
            r = p-t-i+1
            l.append(r)
            for k in range(i-1):
                l.append(1)
            t = p
            break

        t += c 
        l.append(c)
    if t<p:
        return []
    return l

def operate(l, opeL):
    length = len(opeL)
    for i in range(length):
        t = len(l)-(i+2)
        sp = t+opeL[i]
        l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
    return l 

def solve():
    inp = input().split()
    n = int(inp[0])
    p = int(inp[1])
    l = createL(n)
    opeL = operationL(n,p)
    l = operate(l, opeL)
    result = " "
    if opeL:
        for item in l:
            result += str(item)+ " "
    else:
        result =" IMPOSSIBLE"
    print("Case #"+str(i+1)+": "+ str(result))

for i in range(int(input())):
    solve()
"""


"""
Median Sort

//Submitted by Rubleen Kaur
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long int ll;

int main()
{
    ll t,n,q;
    cin>>t>>n>>q;
    while(t-- !=0){
    vector<ll> a;
    
    cout<<"1 2 3"<<endl;
    
    ll size=3;
    ll p;
    cin>>p;
    if(p==2){
        a.push_back(1);
        a.push_back(2);
        a.push_back(3);
        
    }
    else if(p==3){
        a.push_back(1);
        a.push_back(3);
        a.push_back(2);
    }
    else{
        a.push_back(2);
        a.push_back(1);
        a.push_back(3);
    }
    for(ll i=4;i<=(n);i++){
        ll k=0;
        ll r=size-1;
        while(k<r){
            ll mid=k+((r-k)/2);
            cout<<a[mid]<<" "<<a[mid+1]<<" "<<(i)<<endl;
            cin>>p;
            if(p==a[mid]){
                r=mid;
            }
            else if(p==a[mid+1]){
                
                k=mid+1;
            }
            else{
                a.insert(a.begin()+mid+1,i);
                size++;
                break;
            }
        }
        if(size!=i){
            if(k==0){
                a.insert(a.begin(),i);
            }
            else{
                a.push_back(i);
            }
            size++;
        }
    }
    for(auto arr: a){
        cout<<arr<<" ";
    }
    cout<<endl;
    cin>>p;
    if(p==-1){
        break;
    }
}
}
"""

"""
Reverse Engineering 

def process_input(inputs):
    output = []

    for input in inputs:
        T = int(input[0])
        C = int(input[1])

        min = T-1
        max = T*(T+1)/2 - 1

        if min <= C <= max:
            Cprime = C-T+1
            scores = []
            for i in reversed(range(T)):
                if Cprime == 0:
                    break
                elif i<=Cprime:
                    scores.append(i)
                    Cprime -= i
            out = list(range(1,T+1))
            print (scores)
        else:
            output.append("IMPOSSIBLE")



    return output


if __name__ == "__main__":
    n = int(input())
    inputs = []
    for _ in range(n):
        str = input()
        inputs.append(str.split(" "))

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
"""