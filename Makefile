HOST=127.0.0.1
PORT=80
# https://www.data.gouv.fr/fr/datasets/voies-reseau-routier/#_
ROAD_DB=https://www.data.gouv.fr/fr/datasets/r/84676c65-af40-42c4-b24a-79eecbbcf571

.DEFAULT_GOAL := help

.PHONY: help
help: ## The help command, https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@echo "Social_road help"
	@echo ""
	@cat $(MAKEFILE_LIST) | grep -e "^[a-zA-Z_\-]*: *.*## *" | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: requirements
requirements: ## Install python's requirements
	python -m pip install --upgrade pip
	pip install --no-cache-dir -r requirements.txt

.PHONY: install
install: requirements ## Install all dependances (only on debian-base system)
	apt-get update
	apt-get install -y gdal-bin python3-gdal proj-bin

.PHONY: road-db
road-db: ## Download and load's the road database, https://www.data.gouv.fr/fr/datasets/voies-reseau-routier/#_
	wget -c $(ROAD_DB) -O voies_mel.zip
	unzip	voies_mel.zip
	python manage.py shell --command="from world import load; load.run()"

.PHONY: migrate
migrate: ## Make django makemigrations and migrate it
	python manage.py makemigrations
	python manage.py migrate

.PHONY: run
run: ## Run the developpement server
	python manage.py runserver --host $(HOST) --port $(PORT)

.PHONY: clean
clean: ## Remove file generate by test
	rm -f coverage.xml .coverage
	rm -fR .pytest_cache

include Makefile.test
include Makefile.docker
