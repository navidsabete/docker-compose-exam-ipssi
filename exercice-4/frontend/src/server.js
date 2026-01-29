const express = require("express");
const path = require("path");

const app = express();

const FRONTEND_PORT = process.env.FRONTEND_PORT;

const usersRoutes = require("./routes/users");
const torRoutes = require("./routes/tor-users");


app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// fichiers statiques
app.use(express.static(path.join(__dirname, "public")));

// routes métier
app.use("/users", usersRoutes);
app.use("/tor-users", torRoutes);

// home
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(FRONTEND_PORT);

