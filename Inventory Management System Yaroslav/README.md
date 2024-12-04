# HOW TO RUN IT?

Well, thats easy:
1. Create a virtual enenvironment with comand ```py -m venv env``` in console
2. Activate virtual environment in console:
```env\Scripts\activate```
3. Install dependents:
```pip install fastapi uvicorn```
4. Run uvicorn server using comand:
```uvicorn main:app --reload```

# AND HOW TO TEST IT?

Also easy, go to [Swagger](http://127.0.0.1:8000/docs), there you will find all the endpoints