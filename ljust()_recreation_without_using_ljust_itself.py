#create a function for left justify that takes in the string input and spaces
def left_just(string_input, width):
    total_width = max(width - len(string_input), 0) 
    return((string_input)+(" "*total_width)) 

#create a variable for string input, and width
string_input = input("input a string: ")
width = int(input("input how many spaces for the left justification: "))

#add a print statement 
print(left_just(string_input, width), "Hello, have a good day")