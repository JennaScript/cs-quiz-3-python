# Quiz 3: Question 4

# Old Code:
def c(a):
    b=0
    for i in a:
        b+=i
    return b
print (c([4,5,2,-3]))

# The code above works but is not very descriptive at all in what the function is. 

# New Code: 
# This function will sum up integers in the list provided.

def get_sum(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum

print(get_sum([4, 5, 2, -3]))