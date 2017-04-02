"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib
import sys

result_dict = {}

# Fire query to google knowledge base graph
def getResult(keyword):
	api_key = open('api_key.txt').read()
	query = keyword
	service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
	params = {
	    'query': query,
	    'limit': 10,
	    'indent': True,
	    'key': api_key,
	}
	url = service_url + '?' + urllib.urlencode(params)
	response = json.loads(urllib.urlopen(url).read())
	return result_to_json(response['itemListElement'])

def result_to_json(response_dict):
	count_int = 0
	for element in response_dict:
		count = str(count_int)
		result_dict.update({count : {}})
		if 'description' in element['result']:
			result_dict[count]['description'] = element['result']['description']
		if 'image' in element['result']:
			result_dict[count]['image'] = element['result']['image']['contentUrl']
		if 'detailedDescription' in element['result']:
			if 'url' in element['result']['detailedDescription']:
				result_dict[count]['url'] = element['result']['detailedDescription']['url']
			if 'articleBody' in element['result']['detailedDescription']:
				result_dict[count]['article'] = element['result']['detailedDescription']['articleBody']
		result_dict[count]['type'] = element['result']['@type']
		result_dict[count]['name'] = element['result']['name']
		result_dict[count]['id'] = element['result']['@id']
		count_int += 1
	return result_dict