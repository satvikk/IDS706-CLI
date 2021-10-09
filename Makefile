install:
	pip3 install -r requirements.txt
	
build:
	pip3 install --editable .
test:
	python3 -m pytest -vv checkifup_test.py