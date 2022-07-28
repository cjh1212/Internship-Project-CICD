import requests

def response_test():
    response = requests.post(
        'http://localhost:5000/result',
        data = {
            'sentnce': 'ddd dd efqwecd dfe'
        }
    )

    return response.status_code
 
def test_function():
    assert response_test() == 200
