
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared is not 4")
    else:
        print("correct!")

    if square(3) != 9:
        print("3 squared is not 9")
    else:
        print("correct!")


main()



#-----------------------------------------

from calculator import square

def main():
    test_square()

def test_square():
    try:
       assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squard is not 9")



if __name__ == "__main__":
    main()

#--------------------------------------------------------

from calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


if __name__ == "__main__":
    main()



#--------------------------------------------------------------------

import pytest
from calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()

#------------------------------------------------------------------