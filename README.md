# Web Scraping With AWS

## Introduction
This is a web scraping project that is built using AWS - the goal here is to demonstrate expertise in building a functional Extract Transform Load (ETL) Application on AWS. Hopefully, this project will not cost me an arm and a leg with the AWS bill. 

## Objectives
By the end of this project, the following will have been completed -
1. Create a Python script to scrape product data from the major grocery stores in South Africa. 
2. Scraped data should be processed and then stored in AWS S3.
3. Create detailed logs for the scrapping process and the logs should be stored in AWS S3.
4. Implement scheduler for periodic scraping. 

## Architecture
![Architecture of the web scraping project.](assets/images/woolworths_scrape-AWS.drawio.png)

### Python Engine
The Python Engine is composed of three `modules` which work together to achieve the web scraping functionality.

#### selenium_scrape.py [include hyperlink]
1. extract_number_from_string
2. `create_driver()`:
This solution uses `Selenium` ChromeWebdriver for automation of a Google Chrome browser. 
![Process flow diagram for the create_driver method.](assets/images/process_flow_create_driver.png)

3. `url_scraper(category_url, store)`:
This method returns a list of URLs collected from a category page - e.g. `www.store.co.za/Meat_and_Chicken`. The method takes in the category url and the store which the category url belongs. 
![Process flow diagram for the url_scraper method.](assets/images/url_scraper.png)
    1. `get_woolworth_urls(driver)`: Get the list of product URLs belonging in Woolworth category pages.
    ![Process flow diagram for method used to get list of woolworth product urls.](assets/images/process_flow_woolworth_urls.png) 
        a. `get_woolies_product_data(csv_file_path)`: This function accesses a csv containing the product urls from woolworth, and scrapes their webpage to collect information such as name, price, category, weight.
        ![Process flow diagram for method used to get product data from woolworth product urls.](assets/images/woolworht_product_data.png)
    2. get_checkers_urls
        a. click_next_page_button_checkers
        b. get_checkers_price
        c. get_checkers_product_data



