require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 63d7b0ceea3a07803ac4e808caaa08d51e619bac'
}
clnt = HTTPClient.new
response = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})

output = File.open("/tmp/17","w") #specify what file to store output
output << response 
output.close

puts ("The file was saved!")
