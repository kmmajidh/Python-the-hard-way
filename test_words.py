import classly

def test_words():
    actual = classly.words("aa nn hh hh uuh gg")
    expected = 6
    assert actual == expected
    
