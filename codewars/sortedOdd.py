def sort_array(source_array):
    # Return a sorted array.
    o = iter(sorted(e for e in source_array if e%2))    
    return [next(o) if e%2 else e for e in source_array]
print(sort_array([5, 3, 2, 8, 1, 4]))