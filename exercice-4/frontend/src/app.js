const express = require('express');

const app = express();
const FRONTEND_PORT = process.env.FRONTEND_PORT;
const BACKEND_URL = process.env.BACKEND_URL;
const BACKEND_PORT = process.env.BACKEND_PORT;

html = `
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <title>Random Users via Tor</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
    .users {
      display: flex;
      gap: 20px;
      margin-top: 20px;
      flex-wrap: wrap;
    }
    .user {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: center;
      width: 150px;
    }
    img {
      width: 100px;
      border-radius: 50%;
    }
  </style>
</head>
<body>

  <h1>Utilisateurs récupérés via Tor</h1>
  <button onclick="loadUsers()">Rafraîchir</button>

  <br/>  <br/>

  <div class="users" id="users"></div>
    <script>
        async function loadUsers() {
        const container = document.getElementById("users");
        container.innerHTML = "<p>Chargement...</p>";
        try {
        const response = await fetch("/backend/random-users");
        const users = await response.json();
        container.innerHTML = "";
        users.forEach(user => {
          const divUser = document.createElement("div");
          divUser.className = "user";
          divUser.innerHTML = \`
            <img src="\${user.picture}" />
            <p>\${user.name}</p>
          \`;
          container.appendChild(divUser);
          });
            } catch (error) {
        container.innerHTML = "<p>Erreur lors du chargement</p>";
      }
    }
        // Chargement automatique au démarrage
    loadUsers();
  </script>
</body>
</html>
  `;

app.get("/random-users", async (req, res) => {
    res.send(html);
});

app.get("/backend/random-users", async (req, res) => {
    try {
    const response = await fetch(
      `${BACKEND_URL}:${BACKEND_PORT}/tor-api/random-users`
    );
    const user = await response.json();
    res.json(user);
    } catch (err) {
    res.status(500).json({ error: "Backend unreachable" });
  }
});

app.listen(FRONTEND_PORT);
