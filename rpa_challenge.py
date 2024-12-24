from playwright.sync_api import sync_playwright
import pandas as pd
from pathlib import Path
from time import sleep

with sync_playwright() as p: 

    browser = p.chromium.launch(headless=False)  
    page = browser.new_page()
    page.goto('https://rpachallenge.com')

    start_button = page.locator('body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.instructions.col.s3.m3.l3.uiColorSecondary > div:nth-child(7) > button')
    start_button.click()

    download_button = page.locator('body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.instructions.col.s3.m3.l3.uiColorSecondary > div:nth-child(7) > a')
    download_button.click()

    with page.expect_download() as download_info:
        download = download_info.value

    download_path = download.path()

    downloaded_file = Path(download_path)

    if downloaded_file.exists():
        df = pd.read_excel(downloaded_file)
        print("Arquivo Excel carregado com sucesso!")
    else:
        print("O arquivo de download não foi encontrado.")
    print(df)

    sleep(1)

    for i, row in df.iterrows():
        campo_first_name = row ['First Name']
        campo_last_name = row ['Last Name ']
        campo_company = row ['Company Name']
        campo_role = row ['Role in Company']
        campo_address = row ['Address']
        campo_email = row ['Email']
        campo_phone = row ['Phone Number']

        page.fill('[ng-reflect-name="labelEmail"]', campo_email)
        page.fill('[ng-reflect-name="labelAddress"]', campo_address)
        page.fill('[ng-reflect-name="labelCompanyName"]', campo_company)
        page.fill('[ng-reflect-name="labelLastName"]', campo_last_name)
        page.fill('[ng-reflect-name="labelRole"]', campo_role)
        page.fill('[ng-reflect-name="labelFirstName"]', campo_first_name)
        page.fill('[ng-reflect-name="labelPhone"]', str(campo_phone))

        submit_button = page.locator('body > app-root > div.body.row1.scroll-y > app-rpa1 > div > div.inputFields.col.s6.m6.l6 > form > input')  # substitua pelo seletor real do botão
        submit_button.click()
    sleep(2)
    browser.close()

