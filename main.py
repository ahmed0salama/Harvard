def function(f):
    print("Before function call")
    f()
    print("After function call")

# @function
def say_hello():
    print("Hello!")


# say_hello()
function(say_hello)