import requests

def response_test():
    response = requests.post(
        'http://34.64.254.235:5001/result',
        data = {
            'sentence': 'ddd dd efqwecd dfedd'
        }
    )

    return response.status_code
 
def test_function():
    assert response_test() == 200