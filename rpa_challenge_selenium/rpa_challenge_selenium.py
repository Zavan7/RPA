from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd


DIRETORIO = Path(__file__).parent
DRIVER = str(DIRETORIO / 'driver' / 'chromedriver.exe')
CAMINHO_ARQUIVO = str(DIRETORIO / 'challenge.xlsx')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": str(DIRETORIO),
    "download.prompt_for_download": False,
    "profile.default_content_settings.popups": 0,
    "directory_upgrade": True
})
chrome_service = Service(executable_path=DRIVER)
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)
TIME_TO_WAIT = 1

chrome_browser.get('https://rpachallenge.com/?lang=EN')
sleep(1)

button_aparecer = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.instructions.col.s3.m3.l3.uiColorSecondary > div:nth-child(7) > button'))
)

button_aparecer.click()

download = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.instructions.col.s3.m3.l3.uiColorSecondary > div:nth-child(7) > a'))
)
download.click()

sleep(2)

df = pd.read_excel(str(CAMINHO_ARQUIVO))
print(df)

for i, row in df.iterrows():
    first_name = row ['First Name']
    last_name = row ['Last Name ']
    company_name = row ['Company Name']
    role_in_company = row ['Role in Company']
    address = row ['Address']
    email = row ['Email']
    phone_number = row ['Phone Number']

    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]').send_keys(first_name)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]').send_keys(last_name)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]').send_keys(company_name)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]').send_keys(role_in_company)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]').send_keys(address)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]').send_keys(email)
    chrome_browser.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]').send_keys(str(phone_number))

    submit_button = chrome_browser.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

print('Sucesso.')
sleep(5)