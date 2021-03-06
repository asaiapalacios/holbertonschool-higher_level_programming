var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 149185fe4572831c683f826350f65387fa9777aa'
    }
}

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}

var req = https.request(options, (res) => {
    streamToString(res, function(jsonString) {
	console.log(typeof jsonString);
	console.log(jsonString);
    });
});
req.end();

req.on('error', function(e) {
    console.error(e);
});
