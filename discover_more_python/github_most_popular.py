import urllib2

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 27aa992fd7186938f589f8b6da49a7264dcc808a'
}

githuburl = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

req = urllib2.Request(githuburl, headers=request_headers)
response = urllib2.urlopen(req) # Call is made
print response.read() # Print response in standard output
