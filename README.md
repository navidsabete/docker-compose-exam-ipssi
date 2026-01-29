# Docker Compose Exam - IPSSI

**Objectif :** mettre en place une architecture Docker complète et modulaire, évoluant sur plusieurs exercices, orchestrée par **Docker Compose**.

Le projet est piloté via un **Makefile**. Commandes disponibles sur le fichier Makefile de l'exercice.

----

**⚙️ Variables d'environnement et configuration**

Les variables sont définis dans un fichier *.env*
Vous trouverez le modèle on *env.template* et *{service}-template.env* que vous aurez besoin de copier dans votre propre fichier *.env* sur votre machine. Affectez ensuite la valeur que vous souhaitez sur chaque variable.

Configuration PgAdmin via le fichier *pgadmin_servers.json*.

## Évolution des exercices

Le projet évolue progressivement d’une architecture simple frontend/backend (exercice 1), vers une gestion de données avec SQLite (exercice 2), l'intégration du réseau Tor pour les appels externes (exercice 3), puis une stack finale complète avec PostgreSQL et PgAdmin (exercice 4).

## Fonctionnalités

- Backend
    - API
    - CRUD sur une ressource `user` (username, password)
    - Stockage des données dans PostgreSQL (SQLite sur l'exercice 2)
    - Appels à une API externe via le réseau **Tor (SOCKS5)**

- Frontend
    - Interaction avec toutes les opérations CRUD
    - Affichage des utilisateurs externes (nom + photo)

- Base de données
    - PostgreSQL persistante via volume Docker
    - Administration via PgAdmin
    - SQLite sur l'exercice 2

----

### 🚀 Lancement du projet

```bash
make all
```