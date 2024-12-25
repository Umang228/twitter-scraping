# Twitter Web-Scraping App
In this repository it was created by using Selenium script that can read the Twitter home page (on your local computer) and fetch the top 5 trending topics under “What’s Happening” section from the homepage. 

## Technologies Used:
1. Selenium: Selenium is a popular tool for automating web browsers. In this project, it is used for web scraping to interact with the Twitter website and extract trending topics.
2. MongoDB: MongoDB is a NoSQL database program. It is used to store the scraped data (trending topics) in a database for persistence.
3. HTML and Jinja: HTML is used to structure the web pages, while Jinja is a templating engine for Python that is used with Flask to generate dynamic HTML content. 
4. Python-Dotenv: Python-Dotenv is a Python library that manages environment variables stored in a .env file. It is used in this project to securely store sensitive information such as credentials.
5. Flask: Flask is a micro web framework written in Python. It is used to build the web application and define routes for handling HTTP requests.

### Installation

```bash
pip install -r requirements.txt
```
Set up your environment variables by creating a .env file in the project directory and adding the necessary credentials:

```makefile
proxymesh_user=your_proxymesh_username
proxymesh_pass=your_proxymesh_password
X_EMAIL=your_twitter_email
X_PASS=your_twitter_password
X_USER=your_twitter_username
MONGODB_URI=your_mongodb_uri
```
Usage
Run the Flask application:

```bash
python Web.py
```
Open your web browser and go to http://localhost:5000 to access the web interface.


