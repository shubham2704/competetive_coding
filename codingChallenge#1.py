"""
username = '@kashmira__02'

from collections import Counter
s=input()
s=s.lower()
d=Counter(s)
if s.isalpha() or (not s.isalnum()):
    for i in list(d):
        if i==' ' or i==".":
            del d[i]
    for k,v in sorted(d.items()):
        print(v,k,end="",sep="")
else:
    pass

"""



"""
username = '@im_ajmal_k'

inp = input().strip().lower()
d = dict()
for char in inp:
    if char.isalpha():
        d[char] = d.get(char,0) + 1

for char,count in sorted(d.items()):
    print(count,end="")
    print(char,end="")
"""



"""
username = '@navin.kodam'

op_text = ""
test_input = [ x for x in input()]
converted = list(set(test_input)) 
converted.sort()
for i in converted :
    op_text += str(test_input.count(i)) + str(i)  
print(op_text[2:])
"""



"""
username = '@ansh_gera'

string = input('Enter a sentence.....')
string1 = string.replace(' ', '').lower()
print(string1)
new = ''

if string1.isalpha():

    for x in string1:
        count = 0
        if x in new:
            pass
        else:
            for y in string1:
                if x == y:
                    count += 1
            new += str(count)[-1] + x

    print(f'The result is......[{new}]')
else:
    print('n')
"""



"""
username = '@priya_kheersagar'

#include <iostream>
#include<cctype>
using namespace std;
int main()
{
    string s;
    getline(cin,s);
    int arr[26]={0};
    for (int i=0;i<=s.size();i++)
    {
        if(isupper(s[i])) s[i]+=32;
        if(islower(s[i])) arr[s[i]-'a']++;
    }
    for(int i=0;i<=25;i++)
        if(arr[i]>0)
            cout<<arr[i]<<(char)(i+'a');
    return 0;
}
"""



"""
username = '@crybot.py'

char= input('Enter a sentence')
ch= ''
out=''
for x in char:
    if x.isupper():
        ch+=x.lower()
    else:
        ch+=x
l1= list(ch)
l1.sort()
for i in range(97,123):
        a = l1.count(chr(i))
        if a==0:
            continue
        else:
            out=out+str(a)+str(chr(i))

print(out)
"""



"""
username = '@_vinosaur_'

d={}
for i in range(97,123):
    d[chr(i)]=0
s=input(' ENTER A STRING ')
for i in s:
    if i in d:
        d[i]+=1
for i in d:
    if d[i]!=0:
        print(" {} {} ".format(d[i],i),end='')
"""



"""
username = '@sumits10300203'

#Method 1
from collections import Counter
inp="this is a test sentence" #put yours
x=list((inp).lower())
x=list(filter(lambda x:x!=" ",x))
x.sort()
i=0
result=""
if not inp.isdigit():
    dic=dict(Counter(x))
    keys=list(dic.keys())
    values=list(dic.values())
    while i!=len(keys):
        result+=str(values[i])+str(keys[i])
        i+=1
print(result)

'''
method 2 without using collections

inp="this is a test sentence" #put yours
x=list((inp).lower())
x=list(filter(lambda x:x!=" ",x))
x.sort()
i=0
result=""
if not inp.isdigit():
    while 1:
        if len(x)==0:
            break
        l1=len(x)
        temp=x[0]
        if temp in x:
            x=list(filter(lambda x:x!=temp,x))
            temp_count=l1-len(x)
        result+=str(temp_count)+temp 
        i+=1
print(result)'''
"""



"""
username = '@navkar_janu2u'

S=input("Enter name")
L=list(S)
L.sort()
print(L)
X=set(L)
X=list(X)
X.sort()
for i in range(len(X)):
    i=X[i]
    c=L.count(i)
    print(i,':',c)
"""