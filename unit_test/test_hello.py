from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_hello():
    assert hello("Diplal") == "hello, Diplal"
    