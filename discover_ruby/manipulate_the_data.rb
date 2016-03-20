require 'HTTPClient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 63d7b0ceea3a07803ac4e808caaa08d51e619bac'
}

clnt = HTTPClient.new
response = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})

my_hash = JSON.parse(response) #stored parsed response in variable my_hash
array_value = my_hash["items"].map { |e| e ["full_name"]} #stored array value in var array_value
puts array_value.join("\n") #prints array_value in format join and next line
