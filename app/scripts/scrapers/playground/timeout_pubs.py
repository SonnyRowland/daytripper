from selenium import webdriver
from selenium.webdriver.common.by import By

pub_names = []

try:
    driver = webdriver.Chrome()
    driver.get("https://www.timeout.com/london/bars-and-pubs/the-best-pubs-in-london")
    publist = driver.find_elements(
        By.CSS_SELECTOR, value="[data-testid='tile-title_testID']"
    )

    pub_names = [
        driver.execute_script("return arguments[0].textContent;", element)
        for element in publist
    ]
    pub_names = [element.split("\xa0")[1] for element in pub_names]

    driver.quit()
except Exception as e:
    print(e)

f = open("../../test/data/timeout_pubs_raw.txt", "a")

for i in range(len(pub_names)):
    f.write(f"{i+1}:{pub_names[i]}\n")
