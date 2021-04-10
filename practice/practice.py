# import sys
# import re
  
# s = next(sys.stdin)

# repeats = r'(.)\1+'
# for match in re.finditer(repeats, s):
#     print(match.group())

from collections import Counter
a='PPQRSSSTPSPTT'
times=3
for n in range(1,len(a)//times+1)[::-1]:
    substrings=[a[i:i+n] for i in range(len(a)-n+1)]
    freqs=Counter(substrings)
    if freqs.most_common(1)[0][1]>=3:
        seq=freqs.most_common(1)[0][0]
        break
print("sequence '%s' of length %s occurs %s or more times"%(seq,n,times))