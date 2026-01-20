const express = require('express');
const app = express();
const FRONTEND_PORT = process.env.FRONTEND_PORT;
const BACKEND_URL = process.env.BACKEND_URL;
const BACKEND_PORT = process.env.BACKEND_PORT;

app.get('/', async (req, res) => {
    const response = await fetch(`${BACKEND_URL}:${BACKEND_PORT}/api/hello`);
    const data = await response.text();
    res.send(`<h1>${data}</h1>`);
});

app.listen(FRONTEND_PORT);
