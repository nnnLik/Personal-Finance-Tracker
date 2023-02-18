run:
	python manage.py runserver 0.0.0.0:8000
migrate:
	python manage.py makemigrations
	python manage.py migrate
all:
	make migrate
	make run