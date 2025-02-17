"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



# def test_goldilocks(capsys):
#     """Check goldilocks returns expected output"""
#     # given
#     inp = [139, 140, 151, 150]; # Length of the bed
#     res = ['Too small!\n', 'Just right. :)\n', 'Too large!\n', 'Just right. :)\n']
    
#     # when
#     for i in range(len(inp)):
#         fxn.goldilocks(inp(i)) # Function to check the preference on the length of bed
#         captured = capsys.readouterr() # Stores the output of the function to be printed

#      #then   
#         assert captured.out == res(i)  # check that the printed message is was what we expect
    

def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    
    # given
    inp = 139; # Length of the bed
    
    # when
    fxn.goldilocks(inp) # Function to check the preference on the length of bed
    captured = capsys.readouterr() # Stores the output of teh function to be printed

    # then
    assert captured.out == 'Too small!\n'  # check that the printed message is was what we expect


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 30 # test input to the function
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21] # Expected output
    
    # when
    out = fxn.fibonacci_stop(inp) # Actual Output

    # then
    assert exp_out == out # If the actual output is not equal to the expected output, function returns an error


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp1 = [-1, 2, 6, 95] # Input for measurements
    inp2 = [1, 0, 0, 0] # Input for status
    exp_out = [-999, 2, 6, 95] # Expected output

    # when
    out = fxn.clean_pitch(inp1, inp2) # Actual output

    # then
    assert exp_out == out # If the actual output is not equal to the expected output, function returns an error
