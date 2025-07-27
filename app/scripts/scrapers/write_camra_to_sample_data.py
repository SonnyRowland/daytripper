"""scrapes data from camra website and writes to json file"""

import json

from selenium import webdriver
from selenium.webdriver.common.by import By

res = []

pub_names = []
pub_addresses = []

try:
    driver = webdriver.Chrome()
    driver.get("https://www.london.camra.org.uk/viewnode.php?id=105284")

    pub_names = driver.find_elements(By.CSS_SELECTOR, "a.title.listitem.pub-guide")
    pub_names_text = [name.text for name in pub_names]

    locations = driver.find_elements(
        By.CSS_SELECTOR, "span[data-lat][data-lng].location"
    )

    for i, location in enumerate(locations):
        lat = location.get_attribute("data-lat")
        lng = locations[i].get_attribute("data-lng")
        full_address = location.text.strip()
        address = " ".join(full_address.split()[:-2])  # pylint: disable=c0103
        postcode = " ".join(full_address.split()[-2:])  # pylint: disable=c0103

        res.append(
            {
                "name": pub_names_text[i],
                "address": address,
                "postcode": postcode,
                "lat": float(lat),
                "lng": float(lng),
            }
        )

    driver.quit()

    with open("../../data/sample_data.json", "w") as f:
        json.dump(res, f)
except Exception as e:
    print(e)
