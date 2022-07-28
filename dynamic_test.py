import requests

response = requests.post(
	'http://localhost:5000/result',
	data = {
		'sentence': 'ddd dd efqwecd dfe'
	}
)

print(response)