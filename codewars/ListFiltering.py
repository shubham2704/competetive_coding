# VERSION-1

def filter_list(l):
  'return a new list with the strings filtered out'
  
  d = [e for e in l if isinstance(e,int)]
    
  return d


# VERSION-2

def filter_list1(l):

    return [e for e in l if isinstance(e,int)]


print(f"Output by VERSION-1 : {filter_list([1,2,'a','b'])}")
print(f"Output by VERSION-2 : {filter_list1([1,2,'a','b'])}")