HOST=127.0.0.1
PORT=80
# https://www.data.gouv.fr/fr/datasets/voies-reseau-routier/#_
ROAD_DB=https://www.data.gouv.fr/fr/datasets/r/84676c65-af40-42c4-b24a-79eecbbcf571

.PHONY: requirements
requirements:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: install
install: requirements
	apt-get update
	apt-get install -y gdal-bin python3-gdal proj-bin

.PHONY: road-db
road-db:
	wget -c $(ROAD_DB) -O voies_mel.zip
	unzip	voies_mel.zip
	python manage.py shell --command="from world import load; load.run()"

.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver --host $(HOST) --port $(PORT)

