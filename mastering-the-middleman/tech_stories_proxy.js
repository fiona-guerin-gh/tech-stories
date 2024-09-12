const http = require('http');
const httpProxy = require('http-proxy');

// Create a proxy server instance
const proxyServer = httpProxy.createProxyServer({});

// Create the main HTTP server
const server = http.createServer((request, response) => {
  // Set the custom header for reverse proxy identification
  request.headers['reverse-proxy'] = 'tech-stories-node-proxy';

  // Forward the request to the target server on localhost:3000
  proxyServer.web(request, response, { target: 'http://localhost:3000' });
});

// Start the server and listen on port 81
const port = 81;
server.listen(port, () => {
  console.log(`Reverse proxy server listening on port ${port}`);
});
