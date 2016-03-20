require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 63d7b0ceea3a07803ac4e808caaa08d51e619bac'
}
clnt = HTTPClient.new #request httpclient access

puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})
