# ML_Price_Estimator
A machine Learning Web app that does price estimation for specific items after the model has been trained on the proper data.

## Abstract
This project houses two versions of a Machine Learning Application that allows the user to pick a model, a dataset (.csv), and the dependent and independent variables to price estimate the value of an object that the user can use a trained model to estimate. It can be used in the live website version or the desktop version that can be downloaded and run locally

## Software Description
- Our program is written in the [Python Programming Language](https://en.wikipedia.org/wiki/Python_(programming_language)).
- Additionally, we used the following libraries in our implementation:
    * [NumPy](https://pypi.org/project/numpy/) - Python library used to access sizable multi-dimensional arrays and matrices and high-end mathematical functions.
    * [Pandas](https://pypi.org/project/pandas/) - Python library used for data manipulation and analysis.
    * [MatPlotLib](https://pypi.org/project/matplotlib/) - Python library used for data visualization.
    * [Flask](https://pypi.org/project/Flask/) - python framework allowing Python to create and host local websites and web-based applications.
    * [Gunicorn](https://gunicorn.org/) - A Python Library used to host our app on Render.co.
    * [Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) - Python library used to encrypt our data.
    * [PyInstaller](https://pyinstaller.org/en/stable/) - A library we attempted to use to create an .exe file of our desktop app.
    * [flaskwebgui](https://github.com/ClimenteA/flaskwebgui) - A python library we used to convert our Flask application into a desktop version.
    * [SQLAlchemy](https://www.sqlalchemy.org/) - A python library to create a database to house the data we use.
    * [WTForms](https://wtforms.readthedocs.io/en/3.0.x/) - A Flask library that allows for quick CSS functions for our frontend UI.

## Files and Directories
* `LICENSE` - Allows other developers to freely use, change, and distribute this software.
* `README.md` - Contains all information for useability of this software.
* `datasets/___.csv` - Holds all the datasets that a user has uploaded to the Application.
* `data/output.ipynb` - Jupyter notebook file containing the program results.
* `templates` -  Holds all the Html files needed to display the UI.
* `scripts` -  The Scripts folder that holds all the files needed to activate the venv.
* `static` - Holds all the static files that flask needs to have seperate to run the application.
* `requirements.txt` - contains the necessary python packages to run the program in an environment.
* `app.py` - The main driver file for our code.
* `Database.db` -  The Database that houses all the stored encrypted data on users.
* `Users` - The folder to house user specific files.

## Setup

Select one of the following:
1. [Clone/Download](https://github.com/KonechyJ/ML_Price_Estimator) the repository from GitHub.
2. Unzip the folder that just downloaded and open with a command prompt or IDE.

## Steps to Run:

### Method 1): 
        1. Download the repo
        2. Activate the Venv
        3. Pip install the requirements.txt
        4. Run the file file app.py with the command. >>python app.py
        5. This will create a local host version of the repo to test and use.

---
### Method 2): 
        1. Go to the Live website: https://ml-price-estimator.onrender.com
        2. This is a Live hosted version of the main branch that is available anywhere.

---
### Method 3):
        1. Download the zip file of our desktop version (located on the branch Joshua_Konechy)
        2. Open a command prompt and navigate to the zip file's location
        3. Activate the Venv by navigating the the zip file ML_Price_Estimator/scripts and run the command activate
        4. Pip install the requirements.txt using the command pip install -r requirements.txt
        5. Now with a venv opened and the requirements installed simply run the app by using the command : python app.py
        6. This will create a desktop version of the app that can be used without an IDE or using the live website


## Steps to use the Application:

1. Once the app is running, Login or create an account
2. In the main dashboard, select the Train button to train a model
3. Upload a .csv file and input all the dependent variables and independent variable. If you want to just test the app, you can use the built in model and dataset.
Type in "Present_Price", "Kms_Driven", "Owner", "no_year", "Fuel_Type_Diesel", "Fuel_Type_Petrol", "Seller_Type_Individual", "Transmission_Manual",  and "Selling_Price" for the dependent variable. Then hit the upload file button.
4. Hit either test performance to see how the model and data set performed or return to the dashboard
5. Then once at the dashboard, go to the Results page. Now that a model has been trained, you can enter in your own data to test the model.
Again, if just wanted to test our app, then simple type in "5.59", "27000", "0", "8", "0", "1", "0", "1",
6. Hit submit data to see the Price Estimation for your object display at the top of the page


## Group Members
Arifulla Shaik, Brent Pfefferle, Joshua Konechy
