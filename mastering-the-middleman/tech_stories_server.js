const http = require('http');

const server = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });

  const reverseProxyHeader = request.headers['reverse-proxy'];

  if (!reverseProxyHeader) {
    response.end('Hello from the tech stories server!');
  } else if (reverseProxyHeader === 'tech-stories-nginx-proxy') {
    response.end('Received request from the tech stories nginx proxy!');
  } else if (reverseProxyHeader === 'tech-stories-node-proxy') {
    response.end('Received request from the tech stories node proxy!');
  }
});

const port = 3000;
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
