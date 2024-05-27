**Hotstar Data Scraping**

This repository contains scripts and data files for scraping data from Hotstar, an Over-The-Top (OTT) platform, including movie and TV show listings.

**Disclaimer**: 
Please note that the scripts provided in this repository are intended for educational purposes only. They are not intended for any commercial or unethical use. The scraping of websites should always be done in accordance with the terms of service and with the permission of the website owner. The authors of this repository are not responsible for any misuse of the provided scripts.

**Scripts**:

- `multiprocessing_hotstar_movies_scrapper.py`: Python script for scraping movie data from Hotstar using multiprocessing.
- `multiprocessing_hotstar_tv_shows_scrapper.py`: Python script for scraping TV show data from Hotstar using multiprocessing.
- `hotstar_image_scrapper/`: Directory containing Jupyter Notebook files for scraping images from Hotstar.
  - `bucket_image_downloader.ipynb`: Notebook for downloading images from a given bucket.
  - `bucket_image_scrapper.ipynb`: Notebook for scraping images from a given bucket.
  - `bucket_vertical_img_scrapper.ipynb`: Notebook for scraping vertical images from a given bucket.
  - `config.json`: Configuration file for the image scraping notebooks.

**Data Files**:

- `hotstar_movies_data.csv`: CSV file containing scraped data of Hotstar movies.
- `hotstar_tv_shows_data.csv`: CSV file containing scraped data of Hotstar TV shows.

**Usage**:

1. Clone the repository to your local machine.
2. Navigate to the `hotstar` directory.
3. Run the desired Python script (`multiprocessing_hotstar_movies_scrapper.py` or `multiprocessing_hotstar_tv_shows_scrapper.py`) to start scraping data.
4. Alternatively, explore the image scraping process using the provided Jupyter Notebook files in the `hotstar_image_scrapper` directory.

