COMPOSE = docker compose
PROJECT_NAME = docker_compose_ipssi
PG_VOLUME := $(shell docker volume ls -q | grep postgres_data)

.PHONY: all, clean, fclean, re, purge, purge_bdd, purge_all

all:
	$(COMPOSE) up -d --build

clean:
	$(COMPOSE) down

fclean: clean
	docker image prune -a -f

re: fclean all

purge: clean
	docker volume rm $(SQLITE_VOLUME)

purge_bdd: clean
	docker volume rm $(PG_VOLUME)

purge_all:
	$(COMPOSE) down -v --rmi all --remove-orphans
	rm -rf frontend/node_modules backend/__pycache__
	all