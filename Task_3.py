'''
Write a function that accepts an array of positive 
integers and returns an array of all prime numbers 
from the given array. A prime number is a number 
that is only divisible by 1 and itself.
'''
def Return_prime_array(input_array):
  status = False
  Output = []
  for num in input_array:
    if num > 1: 
        if num == 2:
            status = True
        else:
            # Iterate from 2 to n / 2 
            for i in range(2, int(num/2)+1): 
              # If input_num is divisible by any number between 
              # 2 and n / 2, it is not prime 
              if (num % i) == 0: 
                status = False
                break
              else: 
                status = True
    else: 
        status = False
    if status == True: 
        Output.append(num)
  return Output
  

print("Will display array of prime numbers from input array")
Result = Return_prime_array([1,2,3,4,5,6,7,8,9,10])
print(Result)
