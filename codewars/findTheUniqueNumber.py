import collections
def find_uniq(arr):
    return sum([item for item,count in collections.Counter(arr).items() if count==1])
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))