def func(list1):
  count = 0
  for i in range(len(list1)):
    if list1[i]!= 0:
      list1[i-count] = list1[i]
    else:
      count += 1 
  for i in range((len(list1) - count), len(list1) ):
    list1[i] = 0
  return list1
  
      
list1 = [0,1,0,3,12]
print(func(list1))