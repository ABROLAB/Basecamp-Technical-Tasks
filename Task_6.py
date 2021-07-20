'''
Write a function that takes two parameters, 
an array and some number. The function should 
determine whether any three numbers in the array 
add up to the number. If it does, the function should 
return the numbers as an array. If it doesn’t, the function should return -1.
Example
Input: [1, 2, 3, 4, 5, 6], 6
Output: [1, 2, 3]
'''
def Add_any_3(int_array,num):
    output = []
    for i in range(len(int_array)):
        first = int_array[i]
        # Since pythons index start from zero
        # next element in the array will be at index i + 1
        for j in range((i+1),len(int_array)):
            sec = int_array[j]
            # Since pythons index start from zero
            # next element in the array will be at index j + 1
            for k in range((j+1),len(int_array)):
                sum_int = first + sec + int_array[k]
                if sum_int == num:
                    res = [first, sec, int_array[k]]
                    output.append(res)
    if output == []:
        return -1
    else:
        return output 
        
Result = Add_any_3([1, 2, 3, 4, 5, 6], 100)
print(Result)
