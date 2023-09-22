import pytest
import numpy as np
import pygrin

# Define some test cases
test_cases = [
    # Test case 1: Default offset
    (1.5, 0.1, 10.0, 0.0, (-14.603865748353549, 0.0, 3.4475050508922784,
                           6.552494949107722, 10.0, 24.60386574835355)),
    
    # Test case 2: Non-zero offset
    (1.5, 0.1, 10.0, 2.0, (-12.603865748353549, 2.0, 5.447505050892278,
                           8.552494949107722, 12.0, 26.60386574835355)),
    
    # Test case 3: Different values for n_0, pitch, and length
    (1.6, 0.2, 8.0, 1.0, (-0.2928143940846031, 1.0, 3.8908208674633746,
                          6.109179132536625, 9.0, 10.292814394084603)),
]

@pytest.mark.parametrize("n_0, pitch, length, offset, expected_values", test_cases)
def test_cardinal_points(n_0, pitch, length, offset, expected_values):
    # Calculate the cardinal points using the function
    result = pygrin.cardinal_points(n_0, pitch, length, offset)
    
    # Check if the calculated values match the expected values
    assert np.allclose(result, expected_values, rtol=1e-6)

# Run the tests
if __name__ == "__main__":
    pytest.main()
