#%%
# Exercice 1 Create a simple function
def greet(name):
    print(f"Hello, {name} !")

# try the function
name = "World"
greet(name)
#%%
# Exercice 2 If/Else statements
def goldilocks(length):
    if length < 140:
        print("Too small!")
    elif length > 150:
        print("Too large!")
    else:
        print("Just right!")

length = 150.1
goldilocks(length)

#%%
# Exercice 3 For loop
def square_list(list):
    squares = []
    for i in list:
        squares.append(i**2)
    return squares

list = [1, 2, 3, 4, 5]
squares = square_list(list)
print(squares)
# %%
# Exercice 4 While loop
def fibonacci_stop(max):
    fibonacci_sequence = [1, 1]
    while fibonacci_sequence[] < max:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

print(fibonacci_stop(30))
# %%
