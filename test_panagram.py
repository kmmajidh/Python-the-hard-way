import classly

def test_panagram_1():
    actual_value = classly.panagram("The quick brown Fox jumps over the lazy dog")
    expected_value = True
    assert actual_value == expected_value

def test_panagram_2():
    actual_value = classly.panagram("aha")
    expected_value = False
    assert actual_value == expected_value

