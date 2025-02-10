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
def fibonacci_stop(max_value):
    fibonacci_sequence = [1, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < max_value:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        #print(fibonacci_sequence)
    return fibonacci_sequence

print(fibonacci_stop(30))
# %%
# Exercise 5 Logical operations
def clean_pitch(pitch, status):
    # check for each pair of pitch and status if status is above 0 and pitch is not between 0 and 90 and correct pitch to -999
    for i in range(len(pitch)):
        if status[i] > 0 and (pitch[i] < 0 or pitch[i] > 90):
            pitch[i] = -999
    return pitch

pitch = [-1, 2, 6, 95]
status = [1, 0, 0, 0]  
print(clean_pitch(pitch, status))

# %%