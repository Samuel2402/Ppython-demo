def array123(ints):
    array_len = len(ints)-2
    for i in range(array_len):
        if ints[i] == 1 and ints[i+1] == 2 and ints[i+2] == 3:
            return True
    else:
        return False


















def array123(ints):
    array_len = len(ints)
    for i in range(array_len):
        if ints[i,i+1,i+2] == [1, 2, 3]:
            return True 
   else:
       return False
