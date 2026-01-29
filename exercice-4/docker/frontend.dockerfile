FROM node:20-slim

WORKDIR /app
COPY frontend/src/ /app/

RUN npm init -y && npm install express

EXPOSE 3000
CMD ["node", "server.js"]