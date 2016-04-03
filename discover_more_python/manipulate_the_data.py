import urllib2
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 27aa992fd7186938f589f8b6da49a7264dcc808a'
}

githuburl = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

req = urllib2.Request(githuburl, headers=request_headers)
response = urllib2.urlopen(req) # Call is made

parsed_json = json.loads(response.read()) # Parsed JSON into a Python dictionary 

for i in range(0, 30): # Set for loop to display full names of the 30 most popular projects
   print parsed_json['items'][i]['full_name'] 
