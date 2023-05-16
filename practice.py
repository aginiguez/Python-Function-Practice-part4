# Define the max_num() function
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(67, 1, 1000))  

# Define the mult_list() function
lst = [1, 2, 3, 4] # global variable

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num #result = result * num
    return result

print(mult_list(lst)) 

# Define the rev_string() function

def rev_string(s):
    return s[::-1] # slicing notation

print(rev_string("hope"))   # Output "epoh"

# Define the num_within() function
def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

print(num_within(3, 2, 4))   # True
print(num_within(3, 1, 3))   # True
print(num_within(10, 2, 5))  # False


# Define the pascal() function
def pascal(n): # n is the number of rows 
    row = [1] # First row 
    y = [0] # Second row & its a 0 because we want to add the first row and second row together 
    for x in range(max(n,0)): 
        print(row) 
        row=[l+r for l,r in zip(row+y, y+row)] # A for loop to iterate through the list and zip() to iterate through the list and add the elements together
    return n>=1 # print out the first n rows of Pascal's triangle 

n = 14
pascal(n) # Pascal's triangle an arithmetic and geometric figure first imagined by Blaise Pascal 
