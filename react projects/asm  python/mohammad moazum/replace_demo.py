import re 
s='hello how are 234 and 6578'
pat=input('enter any pattern:')
s1=re.sub(pat,'ABC',s)
print(s1)
