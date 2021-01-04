# Insertion Sort

## Pseudocode

```
  InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

## Sample Arrays

Input array:

[8,4,23,42,16,15]

Step through:

**8** -> does not have a previous so it is considered sorted  -> [8,4,23,42,16,15]
**4** -> compared to 8, moved before 8  -> [4,8,23,42,16,15]
**23** -> considered sorted -> [4,8,23,42,16,15]
**42** -> considered sorted -> [4,8,23,42,16,15]
**16** -> smaller than 42, moved back and compared to 23, moved back and compared to 4, it is larger than 4 so it is moved after 4 -> [4,8,16,23,42,15]
**15** -> smaller than 42, moved back and compared to 23, moved back and compared to 16, moved back and compared to 4, it is larger than 4 so it is moved after 4 -> [4,8,15,16,23,42]
