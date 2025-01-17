import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from twitter_scrapping import main as run_scraper
from pymongo import MongoClient
import logging

load_dotenv(".env")

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.twitter_trends
collection = db.trends

@app.route('/')
def index():
    # Retrieve data from MongoDB
    trending_data = collection.find_one(sort=[('date', -1)], projection={'_id': False})
    return render_template('index.html', trend=trending_data)

@app.route('/scrape', methods=['POST'])
def scrape():
    logger.info("Scrape route called")
    try:
        run_scraper()
        logger.info("Scraping completed successfully")
    except Exception as e:
        logger.error(f"Error occurred during scraping: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


