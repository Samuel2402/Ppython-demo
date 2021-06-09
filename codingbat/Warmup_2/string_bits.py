def string_bits(str):
  result = ""
  for i in range(len(str)):     # for every value i in range of the string length 
    if i % 2 == 0:              # checks if (i) is an even number (0=even 1=odd)
      result = result + str[i]
  return result
