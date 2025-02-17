# Create a simple function
def greet(name):
    print(f"Hello, {name} !")



# If/Else statements
def goldilocks(length):
    if length < 140:
        print("Too small!")
    elif length > 150:
        print("Too large!")
    else:
        print("Just right!")



#  For loop
def square_list(list):
    squares = []
    for i in list:
        squares.append(i**2)
    return squares


#  While loop
def fibonacci_stop(max_value):
    fibonacci_sequence = [1, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < max_value:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


# Logical operations
def clean_pitch(pitch, status):
    # check for each pair of pitch and status if status is above 0 and pitch is not between 0 and 90 and correct pitch to -999
    for i in range(len(pitch)):
        if status[i] > 0 and (pitch[i] < 0 or pitch[i] > 90):
            pitch[i] = -999
    return pitch
