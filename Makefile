install:
	pip install -U pip
	pip install -r requirements.txt

run:
	python manage.py runserver

collectstatic:
	python manage.py collectstatic

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

shell:
	python manage.py shell

flake:
	@flake8 --statistics .

isort:
	isort -rc -m 3 calc

build: install migrate collectstatic

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
