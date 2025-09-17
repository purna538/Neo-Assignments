import pytest

# ✅ This test will run 3 times, once for each email
@pytest.mark.parametrize("email", [
    "test1@example.com",
    "test2@example.com",
    "test3@example.com"
])
def test_email_format(email):
    print(f"\nRunning test with email: {email}")
    
    # ✅ Simple assertion to validate email contains '@'
    assert "@" in email, f"Email '{email}' is not valid"
