sentence='my name is kumar'
check=" "
word=""
list1=[]
for char in sentence:
  if check==char:
    list1.append(word)
    word=""
  else:
    word+=char
print(list1)