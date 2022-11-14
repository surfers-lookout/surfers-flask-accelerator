
# Test web app home page
def test_home_page(test_client):
    """
    GIVEN Accelerators Home Page
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    _response = test_client.get('/')
    assert _response.status_code == 200
    assert b'Surfers Lookout' in _response.data
    assert b'World' in _response.data


# Test that the 404 error condition is caught as configured
def test_unknown_page(test_client):
    """
    GIVEN An unknown web page to ensure 404 caught
    WHEN the '/unknown' page is requested (GET)
    THEN check that the friendly reponse page responds
    """
    
    _response = test_client.get('/unknown')
    assert _response.status_code == 200
    assert b'Page Not Found' in _response.data

