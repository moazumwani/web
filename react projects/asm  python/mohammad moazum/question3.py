s=input('enter the string whose words you want to count:')
words=s.split()
print(words)
count=0
for word in words:
  n=len(word)
  r=n%2
  if r==0:
    count=count+1
print('number of even length words = ',count)   
