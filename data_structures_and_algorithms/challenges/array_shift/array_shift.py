def insertShiftArray(arr , val):
    """
    The function takes in an array and a value
    then inserts the value in the center index 
    of the array.
    """

    if isinstance(arr , list):
        length = len(arr)
        index = 0
        new = []
        
        if length%2 == 0:
            index = length/2
        if length%2 > 0:
            index = length/2 + 0.5

        for x in arr:
            if len(new) == index:
                new.append(val)
            new.append(x)

        if length == 0 or length == 1:
            new.append(val)

        arr = new
        return arr

    return 'Invalid Input'
