a=-123
b=[]
a=str(a)
for each in a:
	b.append(each)
if '-' in b:
	del b[0]
b.append('-')
b.reverse() 
b=''.join(b)
print(b)


