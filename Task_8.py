'''
Write a method to count the number of 3s that appear 
in all the numbers between 0 and n (inclusive). 
It should return an object containing the count of 
the number of 3s that appear and an array of the 
numbers that have 3s in them
Example:
Input: 35
Output: { count: 10, numbers: [3, 13, 23, 30, 31, 32, 33, 34, 35] }
'''

 
# function to display the values
def Count_and_Display(n):
    
    digit = 3
    count = 0
    int_array = []
    
    # Check all numbers one by one
    for num in range(0, n+1):
        #print(num)
        # checking for digit
        for index in str(num):
            if index == str(digit):
                count += 1
                if num not in int_array:
                    int_array.append(num)
            
    Output = {"count": count, "numbers": int_array}        
    return Output
    
print(Count_and_Display(35))
