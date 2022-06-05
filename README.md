Python & pip versions	

	python --version
	py -m pip --version

Installing virtualenv (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)

	py -m venv fastapienv

Activating a virtual environment

	.\fastapienv\Scripts\activate

Install FastAPI


	python -m pip install fastapi uvicorn[standard]
	
Run Api

	uvicorn src.main:app --reload
	
Check the Interactive API Documentation

	http://127.0.0.1:8000/docs

Check the Alternative Interactive API Documentation

	http://127.0.0.1:8000/redoc
	
	
