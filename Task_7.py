'''
Write a function that takes an array of positive 
integers and calculates the standard deviation of 
the numbers. The function should return the standard deviation.
'''
def Calc_Standard_Dev(int_array):
    
    standard_deviation = 0
    sqr_mean = 0
    sqr_array = []
    # step 1: calculate the mean
    mean = sum(int_array)/len(int_array)
    
    # Step 2: subtract each integer from mean then square
    for element in int_array:
        sqr = pow((mean - element),2)
        sqr_array.append(sqr)
    
    # step 3: calculate mean of integers gotten from step 2   
    sqr_mean = sum(sqr_array)/len(sqr_array)
    
    # Step 4: Take the square root of the result in step 3
    standard_deviation = pow(sqr_mean,0.5)  
    
    return standard_deviation
        
Result = Calc_Standard_Dev([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])
print(Result)
