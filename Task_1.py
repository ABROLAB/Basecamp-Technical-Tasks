'''
Tasks
Write a function that takes an array of positive integers. 
The function should calculate the sum of all even and odd 
integers and return an array containing the sums. 
The first index in the returned array should hold the sum 
of the even integers and the second index should hold the 
sum of the odd integers.
'''
def Calculate_Even_Odd_Sum(int_array):
    
  even_array = []
  odd_array = []
  
  for num in int_array:
    if num > 1:
      if (num % 2) == 0:
          even_array.append(num)
      else:
          odd_array.append(num)
  
  sum_even = sum(even_array)
  sum_odd = sum(odd_array)
  
  Output = [sum_even,sum_odd] 

  return Output
  
Result = Calculate_Even_Odd_Sum([1, 4, 6, 4, 7, 4])
print("[Sum of even integers,Sum of odd integers]")
print(Result)
