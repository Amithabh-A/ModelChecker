all:
	python3 -m venv venv && \
	source venv/bin/activate && \
	sleep 0.5 && \
	pip install -r requirements.txt

run:
	python3 driver.py < input.txt

clean : 
	rm parser.out
	rm parsetab.py
	rm -rf __pycache__

exit:
	deactivate && \
	rm -rf venv
