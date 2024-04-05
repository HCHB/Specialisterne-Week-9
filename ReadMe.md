Searching for cereals are done through a query string. 
F.x.

    localhost/cereal?fat=1&calories[lt]=100&calories[gt]=10&shelf=1

The brackets are used for determining what kind of comparison is being performed, where no brackets means a simple equals

    [lt]  = less than
    [leq] = less than or equal
    [gt]  = greater than
    [geq] = greater than or equal
    [ne]  = not equal


How to setup:

	Run lagersystem.sql either in the MySQL workbench or directly in cmd

	Open cmd in the main project folder and run

	python -m venv ./venv
	.\venv\Scrupts\activate
	pip install -r requirements.txt
    python -m src.Data.dataloader
	deactivate

How to run:

	Open cmd in the main project folder and run

	.\venv\Scrupts\activate
	python -m src.main
	deactivate

	Note that there is currently only 1 user: hebo_user - test123