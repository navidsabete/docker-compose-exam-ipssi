COMPOSE = docker compose
PROJECT_NAME = docker_compose_ipssi

.PHONY: all, clean, fclean, re

all:
	$(COMPOSE) up -d --build

clean:
	$(COMPOSE) down

fclean: clean
	docker image prune -a -f

re: fclean all