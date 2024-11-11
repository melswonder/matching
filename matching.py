from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

# コマンドライン引数を取得
if len(sys.argv) != 5:
    print("error main.shを見直してください")
    sys.exit(1)

URL = sys.argv[1]
TIME = sys.argv[2]
INTORA = sys.argv[3]
PASS = sys.argv[4]

# Chrome のオプションを
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # ヘッドレスモードで実行
options.add_argument('--no-sandbox')  # サンドボックス無効化（Linux環境で推奨）
options.add_argument('--disable-gpu')  # GPU無効化（ヘッドレスモードで推奨）

# エラーハンドリングを追加してWebDriverを起動
try:
    driver = webdriver.Chrome()
except Exception as e:
    print(f"Chromeドライバの起動に失敗しました: {e}")
    sys.exit(1)

elements_found = False  # 要素が見つかったかどうかのフラグ

try:
    driver.get(URL)

    target = driver.find_element(By.ID,"username")
    target.send_keys(INTORA)

    target = driver.find_element(By.ID,"password")
    target.send_keys(PASS)

    btn = driver.find_element(By.ID,"kc-login").click()

    while not elements_found:
        time.sleep(0.3) #あるのに見つからない場合は個々の時間を少し伸ばしてください

        # ページ全体から指定したテキスト（TIME）を含む要素を検索
        elements = driver.find_elements(By.XPATH, f'//*[contains(text(), "{TIME}")]')
        count = len(elements)

        if count > 0:
            elements_found = True  # 要素が見つかったらループを抜ける
        else:
            print(f'no matching...')

except Exception as e:
    print(f"error: {e}")
finally:
    if elements_found:
        print(f"matching!!! element count:{count}")
        input("Press Enter to close the browser...") 
driver.quit()
