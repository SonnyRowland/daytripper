from selenium import webdriver
from selenium.webdriver.common.by import By
import json

pub_names = []
pub_addresses = []

try:
    driver = webdriver.Chrome()
    driver.get("https://www.london.camra.org.uk/viewnode.php?id=105284")

    pub_names = driver.find_elements(By.CSS_SELECTOR, "a.title.listitem.pub-guide")
    pub_names_text = [name.text for name in pub_names]

    locations = driver.find_elements(
            By.CSS_SELECTOR, 
            "span[data-lat][data-lng].location"
        )
    
    res=[]

    for i in range(len(locations)):
        lat = locations[i].get_attribute("data-lat")
        lng = locations[i].get_attribute("data-lng")
        address = locations[i].text.strip()

        res.append({
            "name": pub_names_text[i],
            "address": address,
            "lat": float(lat),
            "lng" : float(lng),
        })
    
    json_data = json.dumps(res, indent=2)
    print(json_data)

    driver.quit()
except Exception as e:
    print(e)
