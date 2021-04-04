import requests

# post = requests.post('https://httpbin.org/post')
# put = requests.put('https://httpbin.org/put')
# delete = requests.delete('https://httpbin.org/delete')
#
# print(delete)

parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('http://fabrykatestow.pl', params=parameters)
# print(r.url)
# print(r.text)
# print(r.encoding)