# Quiz 3: Question 1

# The code above has a few errors. There are a ton of syntax errors. First, there is a misspelling of a variable in the function. "num_listt" should be num_list. The return should be sum / len(num_list) if we are trying to get the average. And the print function is missing two parentheses to completely close it. Lastly, the sum should initialize at 0 instead of 1.

# New Code:
def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""
    sum = 0
    for i in num_list:
        sum += i 
    return sum / len(num_list)

print(get_average([1,3,5,6,7]))