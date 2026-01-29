const express = require('express');
const router = express.Router();

const BACKEND_URL = process.env.BACKEND_URL;
const BACKEND_PORT = process.env.BACKEND_PORT;


// Lecture utilisateurs
router.get("/", async (req, res) => {
  const response = await fetch(`${BACKEND_URL}:${BACKEND_PORT}/api/users`);
  const users = await response.json();

  let html = `
    <h1>CRUD Users</h1>
    <form method="POST" action="/users/create">
        <input name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Créer</button>
    </form>
    <h2>Liste des utilisateurs</h2>
    <ul>
    `;
    users.forEach(u => {
        html += `<li>ID: ${u.id} - ${u.username} | Password : ${u.password} |
                    
                      <a href="/users/${u.id}">
                      <button type="button">Voir détails</button>
                      </a>
                    
                    <form method="POST" action="/users/delete/${u.id}" style="display:inline">
                        <button type="submit">Supprimer</button>
                    </form>
                 </li>`;
    });
    html += "</ul>";
    res.send(html);
});

// Création utilisateur
router.post("/create", async (req, res) => {
    await fetch(`${BACKEND_URL}:${BACKEND_PORT}/api/users/create`, {
        method: "POST",
        body: new URLSearchParams({
            username: req.body.username,
            password: req.body.password
        }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    });
    res.redirect("/users");
});

// Détails utilisateur
router.get("/:id", async (req, res) => {
    const userId = req.params.id;
    const response = await fetch(
        `${BACKEND_URL}:${BACKEND_PORT}/api/users/${userId}`
    );

     if (!response.ok) {
        return res.send("<h1>Utilisateur non trouvé</h1>");
    }

    const user = await response.json();

    const html = `
        <h1>Détails utilisateur</h1>

        <p><strong>ID :</strong> ${user.id}</p>

        <form method="POST" action="/users/update/${user.id}">
            <label>
                Username :
                <input name="username" value="${user.username}" required>
            </label>
            <br><br>
            <label>
                Password :
                <input type="password" name="password" required>
            </label>
            <br><br>
            <button type="submit">Mettre à jour</button>
        </form>

        <br>
        <a href="/users">
            <button type="button">Retour à la liste</button>
        </a>
    `;

    res.send(html);
});

// Mise à jour utilisateur
router.post("/update/:id", async (req, res) => {
    const userId = req.params.id;
    await fetch(`${BACKEND_URL}:${BACKEND_PORT}/api/users/${userId}`, {
        method: "PUT",
        body: new URLSearchParams({
            username: req.body.username,
            password: req.body.password
        }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    });
    res.redirect(`/users/${userId}`);
});

// Suppression utilisateur
router.post("/delete/:id", async (req, res) => {
    const userId = req.params.id;
    await fetch(`${BACKEND_URL}:${BACKEND_PORT}/api/users/${userId}`, {
        method: "DELETE"
    });
    res.redirect("/users");
});

module.exports = router;