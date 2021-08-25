// require from CommonJs module system, http module from Node.js library
const http = require('http')


const hostname = '127.0.0.1'
const port = process.env.PORT

// createServer method of http creates server and returns it
// request evetn provides two objects: an incoming message (request) object and a server response (response) object
const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World!\n')
})

// start the server asynchronously listening for connections
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})