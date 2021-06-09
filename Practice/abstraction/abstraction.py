def new_decorator(func):
    def wrap_func():
        print('I run before the exec func')

        func()

        print('Code here after exec func()')
    
    return wrap_func
@new_decorator     # easy way to assign a function to another function 
def fund_needs_decorator():
     print('please decorate me!')

    #func_needs_decorator = new_decorator(function_needs_decorator)    
func_needs_decorator() 