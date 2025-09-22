from gateway.auth import authenticate

def test_authenticate():
    assert authenticate('tenant123-token') == True
    assert authenticate('invalid-token') == False
