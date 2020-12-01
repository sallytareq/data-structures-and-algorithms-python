def binary_search(in_list, x): 
    """
    The function searches a list (in_list) for the value (x)
    and returns the index of that value if it is present in the list, 
    otherwise it returns -1 
    
    NOTE: the function assumes that the list is sorted in an assending order
    """
    # Check type:
    if type(in_list) != list or type(x) != int:
        return 'Invalid Input'

    start = 0
    mid = 0
    end = len(in_list) - 1

    # Special case: when the list contains only one value
    if start == end:
        if in_list[0] == x:
            return 0

  
    while start < end: 
  
        mid = (end + start) // 2

        # checks middle value
        if in_list[mid] == x:
            return mid
  
        # If x is greater than the mid we can ignore the lower half 
        # Set start as mid+1 because x != mid
        if in_list[mid] < x: 
            start = mid + 1
  
        # If x is smaller than the mid we can ignore the upper half 
        # Set end as mid-1 because x != mid
        elif in_list[mid] > x: 
            end = mid - 1

        else: 
            return mid 
  
    
    return -1
  
