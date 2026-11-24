import http from 'node:http';
import { createReadStream, existsSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';

const ROOT = new URL('./app/dist/', import.meta.url).pathname.replace(/^\/(\w:)/, '$1');
const PORT = 4321;
const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.mjs': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
  '.ico': 'image/x-icon', '.txt': 'text/plain', '.xml': 'application/xml', '.woff2': 'font/woff2',
};

http.createServer((req, res) => {
  let urlPath = decodeURIComponent(req.url.split('?')[0]);
  if (urlPath.endsWith('/')) urlPath += 'index.html';
  let filePath = join(ROOT, urlPath);
  if (!existsSync(filePath) || statSync(filePath).isDirectory()) {
    const alt = filePath + '.html';
    if (existsSync(alt)) filePath = alt;
    else { res.writeHead(404); res.end('404'); return; }
  }
  res.writeHead(200, { 'Content-Type': MIME[extname(filePath).toLowerCase()] || 'application/octet-stream' });
  createReadStream(filePath).pipe(res);
}).listen(PORT, '127.0.0.1', () => console.log(`serving app/dist at http://127.0.0.1:${PORT}/`));
