from functions import *
# from functions import fibonacci_stop
# from functions import clean_pitch
# from functions import greet
# from functions import goldilocks

name = "World"
greet(name)

length = 150.1
goldilocks(length)

list = [1, 2, 3, 4, 5]
squares = square_list(list)

print(fibonacci_stop(30.5))

pitch = [-1, 2, 6, 95]
status = [1, 0, 0, 0]  
print(clean_pitch(pitch, status))