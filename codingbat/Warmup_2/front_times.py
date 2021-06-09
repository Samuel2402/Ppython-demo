#def front_times(str, n):
#  if len(str) <= 3:
#    return str
#  frnt = str[:3]
#  else:
#    return frnt*n

def front_times(str, n):            #(chocolate,3)
  front_len = 3                     #(choc)
  if front_len > len(str):          #IF the front_length > the length of the whole string (returns no),(if yes repeat up to 3)
    front_len = len(str)            #front_len will now equal the length of the string 
  front = str[:front_len]           #create new term front, = the string up to the total length of (how long the string is )
  
  result = ""
  for i in range(n):
    result = result + front
  return result
  
  print(chocolate.front_times())