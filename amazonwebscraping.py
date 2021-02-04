#!/usr/bin/env python
# coding: utf-8

# In[103]:


## Amazon Web scraping on suit


# In[104]:


# Navigate to Amazon website
url = "https://www.amazon.com/"
driver.get(url)


# In[ ]:


# Extract Records and Return a single record
def extract_record(item):
    
    # description and url
    search_link = item.h2.a
    description = item.h2.a.text.strip()
    url = "https://www.amazon.com/" + search_link.get('href')
    try:
        # Price
        parent_price = item.find("span", "a-price")
        price = parent_price.find('span', 'a-offscreen').text
    except AttributeError:
        return
    
    try:
        # Ratings and Ratings count
        rating = item.i.text
        rating_count = item.find('span', {'class':'a-size-base'}).text
    except AttributeError:
        rating = " "
        rating_count = " "
        
        
    result = (description, price, rating, rating_count, url)
    
    return result


# In[ ]:


records = []
results = search_results = soup.find_all("div", {"data-component-type" : "s-search-result"})

for item in results:
    record = extract_record(item)
    if record:
        records.append(record)


# # Getting to the Next Page

# In[ ]:


# Import the requir modules
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Get url
def get_url(search_term):
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss"
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)

    # add term query to the url
    url = template.format(search_term)
    
    # add page query placeholder to the url
    url += '&page{}'
    
    return url

# Extract Records and Return a single record
def extract_record(item):
    
    # description and url
    search_link = item.h2.a
    description = item.h2.a.text.strip()
    url = "https://www.amazon.com/" + search_link.get('href')
    try:
        # Price
        parent_price = item.find("span", "a-price")
        price = parent_price.find('span', 'a-offscreen').text
    except AttributeError:
        return
    
    try:
        # Ratings and Ratings count
        rating = item.i.text
        rating_count = item.find('span', {'class':'a-size-base'}).text
    except AttributeError:
        rating = " "
        rating_count = " "
        
        
    result = (description, price, rating, rating_count, url)
    
    return result

# scrape the given site 
def main(search_term):
    # Start the web driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
        
    records = []
    url = get_url(search_term)
    
    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = search_results = soup.find_all("div", {"data-component-type" : "s-search-result"})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    
    
    driver.close()
    
    # Save the records to a csv file
    with open('amazonwebscraping.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Ratings', 'Review Count', 'Url'])
        writer.writerows(records)


# In[105]:


main('joggers')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




