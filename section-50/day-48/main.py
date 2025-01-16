from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Amazon-Basics-Density-Exercise-Recovery/dp/B071P2MQ5D/?_encoding=UTF8&pd_rd_w=SF64u&content-id=amzn1.sym.aeef70de-9e3e-4007-ae27-5dbb7b4a72f6&pf_rd_p=aeef70de-9e3e-4007-ae27-5dbb7b4a72f6&pf_rd_r=88TG2YBH1CPXKRME852X&pd_rd_wg=07VZ8&pd_rd_r=df312afc-75a0-4111-bf73-61f2e7831640&ref_=pd_hp_d_btf_crs_zg_bs_3375251&th=1")
# time.sleep(15)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is {price_dollar.text}.{price_cents.text}")
driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

# driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# driver.close()
driver.quit()