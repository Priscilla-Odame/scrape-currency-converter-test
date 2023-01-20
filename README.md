### SETTING UP PROJECT

- First create a virtual environment with command ```virtualenv venv```
- Activate the virtual environment using ```source venv/bin/activate``` for linux and ```venv\Scripts\activate``` for windows
- Install requirements using command ```pip install -r requirements.txt```
- Run the app with ```uvicorn main:app --reload```
- The url can be found at ```http://127.0.0.1:8000``` and ```http://127.0.0.1:8000/docs``` to view the documentation.

### NB
- If you do not have ```virtualenv``` installed, follow [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-pip) to install it.