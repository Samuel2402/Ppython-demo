import pdb 

def tailRecursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
    pdb.set_trace()
    if factorial == 1:
        return result
    else:
        return tailRecursion((factorial--),(factorial + result))