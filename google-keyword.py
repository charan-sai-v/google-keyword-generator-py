import requests
import json 


# Making a get request
if(True):
	a = input("Enter Your Keyword:")
	url=("http://suggestqueries.google.com/complete/search?client=firefox&hl=en&q="+a)
	headers = {'User-agent':'Mozilla/5.0'}
	response = requests.get(url, headers=headers)
	result = json.loads(response.content.decode('utf-8'))

word=[]
if(len(result[1])==0):
		print("No Keyword Found")
else:
	for word in result[1]:
		print(word)



       

