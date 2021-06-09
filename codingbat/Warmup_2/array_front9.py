def array_front9(numbers):
  array_length = len(numbers)
  if array_length > 4:
    array_length = 4
    
  for i in range(array_length):
    if numbers[i] == 9:
      return True
  else:
    return False