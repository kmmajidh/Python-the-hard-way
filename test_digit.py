import classly

def test_digit():
    actual_value = classly.digits(12345)
    expected_value = 5
    assert actual_value == expected_value
    
