def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqr = sq**0.5
    n = sqr+1
    if int(sqr+0.5)**2 == sq :
        return int(n**2)
    else:
        return -1

print(find_next_square(121))