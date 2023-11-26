import re 
s='hello how are 234 and 6578'
pat=input('enter any pattern:')
result= re.findall(pat,s)
print(result)

