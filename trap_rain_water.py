

def trapRainWater(arr):
  
  res=0
  for i in range(1,len(arr)-1):
    
    left = arr[i]
    
    for j in range(i):
      left = max(left,arr[i])
     
    
    right = arr[i]
    
    for j in range(i+1,len(arr)):
      right = max(right,arr[j])
     
    res+= min(left,right)-arr[i]
  
  return res
