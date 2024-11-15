from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
import json

# コマンドライン引数を取得
# if len(sys.argv) != 4:
#     print("error main.shを見直してください")
#     sys.exit(1)


json_open = open('settings.json', 'r')
json_load = json.load(json_open)
URL = json_load["url"]
INTRA_ID = json_load['intra_id']
PASS = json_load["intra_password"]
TIME = [
    json_load["time"]["monday"],
    json_load["time"]["tuesday"],
    json_load["time"]["wednesday"],
    json_load["time"]["thursday"],
    json_load["time"]["friday"],
    json_load["time"]["saturday"],
    json_load["time"]["sunday"]
]


# Chrome のオプションを
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # ヘッドレスモードで実行
options.add_argument('--no-sandbox')  # サンドボックス無効化（Linux環境で推奨）
options.add_argument('--disable-gpu')  # GPU無効化（ヘッドレスモードで推奨）
# profile
options.add_argument('--user-data-dir=./profile')
options.add_argument('--profile-directory=Default')

# エラーハンドリングを追加してWebDriverを起動
try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"Chromeドライバの起動に失敗しました: {e}")
    sys.exit(1)



elements_found = False  # 要素が見つかったかどうかのフラグ

try:
    driver.get(URL)

    time.sleep(3)
    if(driver.current_url.find("auth.42.fr") != -1):
        target = driver.find_element(By.ID,"username")
        target.send_keys(INTRA_ID)

        target = driver.find_element(By.ID,"password")
        target.send_keys(PASS)

        btn = driver.find_element(By.ID,"kc-login").click()

    while not elements_found:
        driver.get(URL)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="fc-time"]'))
            )
        except Exception as e:
            print(f"Finding element..", e)

        week_grid = driver.find_elements(By.XPATH, '//div[@class="fc-content-skeleton"]//td')
        elements_found = True
        for i in range(7):
            
            time_json = TIME[i]
            day = week_grid[i+1]
            if(not time_json['start'] or not time_json['end']):
                continue
            time_text = f'{time_json["start"]} - {time_json["end"]}'
            elements = day.find_elements(By.XPATH, f'.//*[@class="fc-time"]/span[text()="{time_text}"]')


            if(len(elements) == 0):
                print (f"Time {time_text} not found in {time_json['label']}")
                elements_found = False
            else:
                print (f"Time {time_text} found in {time_json['label']}")

except Exception as e:
    print(f"error: {e}")
finally:
    if elements_found:
        print(f"Matched!!!!")
        input("Press Enter to close the browser...") 
driver.quit()
