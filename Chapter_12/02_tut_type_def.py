# we can define the type of a vaiable at the time of its initallization as follows:
# By using this format (var_name: var_type = value)


# Example:
num : int = 5
name : str = "Harry"
decimal : float = 5.658

# we also used it with function:

def sum(a : int, b : int) -> int:
    return a + b  # Here we are saying that both the inputs are int and the output is also an integer

sum(5,6)
