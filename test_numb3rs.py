from numb3rs import validate

def test_validate_ip():
    assert validate('255.5.4.3') == True
    assert validate('1.2.3.4') == True


def test_unvalidate_ip():
    assert validate('256.3.4.5') == False
    assert validate('255.1..3.4') == False
    assert validate('i.1.3.4') == False