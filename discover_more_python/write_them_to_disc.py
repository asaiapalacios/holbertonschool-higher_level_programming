import urllib2 # Library to access Request function 
import os.path 

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 27aa992fd7186938f589f8b6da49a7264dcc808a'
}

githuburl = 'https://api.github.com/search/repositories?q=language:python&sort=\
stars&order=desc'
req = urllib2.Request(githuburl, headers=request_headers)
response = urllib2.urlopen(req)

#print response.read()

if os.path.exists("/tmp/17"): # If statement to truncate (empty file) if file exists
    f = open("/tmp/17", "w")
    f.truncate()
    f.close()

varfile = open("/tmp/17", "w")

varfile.write(response.read())
varfile.close()
print "The file was saved!"  

