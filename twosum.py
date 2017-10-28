dict={}
a=[1,3,5,9,11]
target=10
for i in range(len(a)):
     if a[i] in dict:
          print(dict[a[i]],i)
    else:
          dict[target-a[i]]=i