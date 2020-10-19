This is the API to compute the sunlight hours of an apartment written in Python. 
This is a simple document to describe the repo, the implementations details and the mathematical model used is available in the document /SunlightDocumentation.pdf.

sunlight/ contains the code of the API.
test/ contains the unit tests for all classes.
/run.py is a runnable script, example of the usage of the API. It requires 4 arguments:
	1. file describing the city (you can use /mycity.txt)
	2. name of the neighborhood
	3. name of the building
	4. apartment number
/run_test.py runs the unit tests