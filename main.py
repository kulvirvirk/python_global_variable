
# 1. Define a global variable 
# 2. use it in the function 
# 3. use it outside of function 

# 1. Define a global variable 
global_var = 'I am global variable!'

# 2. use it in the function 
def call_global_var():
  print('Using global varibal inside the function: ' + global_var)

call_global_var()

# 3. use it outside of function 
print('Using global varibal outside the function: ' + global_var)


