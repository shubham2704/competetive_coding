from collections import Counter

def string_letter_count(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return ''.join(str(n)+c for c,n in sorted(cnt.items()))

submissionLink = 'https://docs.google.com/forms/d/e/1FAIpQLSdvCKLUV1fuapmRnnUQ8EH0I42A6E-yUKtU4CK2A4CIBjLvlg/viewform?usp=pp_url&entry.1449005772=Your+Name&entry.1685270148=Your+Instagram+Username'