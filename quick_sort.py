'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def quickSort(arr,low,high):
    
    if low>=high:
        return
    
    p = partition(arr,low,high)
    
    quickSort(arr,low,p-1)
    quickSort(arr,p+1,high)



def partition(arr,low,high):
    
    i = low-1
    p = arr[high]
    
    for j in range(low,high):
        if arr[j] < p:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return i+1


a = [-2,-3,0,7,3,2,-5,10,8]

quickSort(a,0,len(a)-1)
print(a)
