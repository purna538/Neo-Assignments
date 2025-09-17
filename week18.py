# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Test the function
if __name__ == "__main__":
    test_str = "Quality Assurance"
    reversed_str = reverse_string(test_str)

    print("Original String:", test_str)
    print("Reversed String:", reversed_str)

    # Fixed assertion
    assert reversed_str == "ecnarussA ytilauQ", "Test Failed!"
    print("✅ Test Passed")
