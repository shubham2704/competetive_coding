# Method 1
def autoMorphic(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!" 

print(autoMorphic(25))
print(autoMorphic(13))

# Method 2
def Automorphic(n):
    return "Automorphic" if str(n) in str(n*n) else "Not!!"
print(Automorphic(25))
print(Automorphic(12)) 