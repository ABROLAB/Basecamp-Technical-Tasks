'''
Write a function that accepts a positive integer 
and determines if it is a prime number. The 
function should return true if it is a prime 
number or false if it isn’t.
'''
def Determine_if_Prime():
  input_num = int(input("Enter your value: "))
  Output = False
  if input_num > 1:
    if input_num == 2:
        Output = True
    else:
        # Iterate from 2 to n / 2 
        for i in range(2, int(input_num/2)+1): 
          # If input_num is divisible by any number between 
          # 2 and n / 2, it is not prime 
          if (input_num % i) == 0: 
            Output = False
            break
          else: 
            Output = True
  else: 
    Output = False
  return Output
  

print("Will display True if number is prime else false")
Result = Determine_if_Prime()
print(Result)
