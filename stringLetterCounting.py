from collections import Counter

def string_letter_count(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return ''.join(str(n)+c for c,n in sorted(cnt.items()))