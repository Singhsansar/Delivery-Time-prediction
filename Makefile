install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test: 
	python -m pytest -vv --cov=app test_app.py

format: 
	find . -type d -name '.venv' -prune -o -type f -name '*.py' -exec black {} +

lint: 
	pylint --disable=R,C *.py

all: install lint test format
