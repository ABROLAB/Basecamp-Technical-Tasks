'''
Write a method to replace all spaces in a string with '%20'.
Example

Input: "Mr John Smith " 

Output: "Mr%20John%20Smith"
'''
def Replace_spaces():
    inp_str = input('Enter String/Sentence: ')
    # Replace() replaces a substring e.g. spaces (" ") in a String
    # with another string e.g. %20
    output = inp_str.replace(" ",'%20')
        
    return output #returns the modified string
    
Result = Replace_spaces()
print(Result)
