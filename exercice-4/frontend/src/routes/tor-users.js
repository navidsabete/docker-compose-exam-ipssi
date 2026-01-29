const express = require("express");
const path = require("path");
const router = express.Router();

const BACKEND_URL = process.env.BACKEND_URL;
const BACKEND_PORT = process.env.BACKEND_PORT;


router.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "tor.html"));
});

router.get("/backend/random-users", async (req, res) => {
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


module.exports = router;
