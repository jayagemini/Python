def add(a, b):
    return a + b 


def test_add():
    # Test cases for the add function
    assert add(1, 2) == 3, "Test case 1 failed"
    assert add(-1, 1) == 0, "Test case 2 failed"
    assert add(0, 0) == 0, "Test case 3 failed"
    assert add(-1, -1) == -2, "Test case 4 failed"
    assert add(1.5, 2.5) == 4.0, "Test case 5 failed"
    assert add(1.5, 2.5) == 4.0, "Test case 5 failed"
    print("===============================")
    print("All test cases passed!")

# Run the test function
test_add()
