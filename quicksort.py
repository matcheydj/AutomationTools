def partition(list,start,end):
  pivot=start
  storeIndex=start
  for i in range(start+1,end+1):
    if i > end:
       break
    if list[i] < list[pivot]:
     temp=list[storeIndex+1]
     list[storeIndex+1]=list[i]
     list[i]=temp
     storeIndex+=1
  tmp=list[storeIndex]
  list[storeIndex]=list[pivot]
  list[pivot]=tmp
  print "storeIndex is "+str(list[storeIndex])
  print "pivot is "+str(list[pivot])
  print list
  return storeIndex

def quicksort(list,start,end):
  if start > end:
    return
  i=partition(list,start,end)
  quicksort(list,start,i-1)
  quicksort(list,i+1,end)

arr=[23,1,54,6,75,12,67,3,12]
quicksort(arr,0,len(arr)-1)
print arr
