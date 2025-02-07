global_var = "I am a global variabl"
def my_function():
    local_var = "I am a local variable"
    print(local_var)

def another_function():
    print(global_var)
my_function()

another_function()




global_var = "I am a global variable"
def global_scope():
    local_var ="I am a local variable"
    print("Inside the function:")
    print("Local variable:", local_var)
    print("Global variable:", global_var)
    return local_var
local_var = global_scope()
print("\nOutside the function:")
print("Global variable", global_var)
print("Local variable:", local_var)
