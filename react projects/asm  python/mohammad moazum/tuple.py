t=(10,20,30,40,50);
n=len(t)
print(t)
L=list(t);
L.append(60);
print(L)
t=tuple(L)
print(t)
d={'m':'monday' , 's':'sunday' ,'t':'tuesday'}
print(d['t'])
d['w']='wednesday'
d['s']='saturday'
print(d)
k=d.keys()
print(k)
v=d.values()
print(v)
s='hello how are you'
n=len(s)
print(n)
print(s[6:9])
print(s[-1])
print(s[ : :-1])
words=s.split()
print(words)
print(words[-1])
print(words[-1][-1])
s1=':'.join(words)
print(s1)
s2=' '.join(words)
print(s2)
