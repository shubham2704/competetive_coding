for _ in range(int(input())):
    n = str(int(input()))
    if n.count('3')+n.count('7')==len(n): print('LUCKY')
    else: print('BETTER LUCK NEXT TIME')