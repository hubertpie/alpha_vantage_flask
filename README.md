# Currency exchange
## Little web application to view exchange rate from alpha vantage API

### Installation (windows)
Add first virtualenv and activate them
```
python -m venv myenv
myenv\Scripts\activate
```
Then install packages from requirements.txt
```
pip install -r requirements.txt
```
You need API key from https://www.alphavantage.co/ to get exchange rate of currencies and create secrets.py file containing API_KEY from site.
Lastly you have to set FLASK_APP to application.py and run server in command line


```bash
set FLASK_APP=application.py
flask run
```
If everything went fine you will see in command line
```
 * Serving Flask app "application.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

***Then you can open browser and go to http://localhost:5000***
