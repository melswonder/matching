
# Install Dependencies
```shell
pip install selenium
```


# 設定
### settings.json example
#### urlには、レビュー予約画面のURLを指定
#### time複数入力時は、すべてが表示されるまでリロードします。
```json:settings.json

{
  "url": "https://profile.intra.42.fr/slots",
  "time": {
    "monday": {
      "label": "Monday",
      "start": "",
      "end": ""
    },
    "tuesday": {
      "label": "Tuesday",
      "start": "",
      "end": ""
    },
    "wednesday": {
      "label": "Wednesday",
      "start": "",
      "end": ""
    },
    "thursday": {
      "label": "Thursday",
      "start": "",
      "end": ""
    },
    "friday": {
      "label": "Friday",
      "start": "",
      "end": ""
    },
    "saturday": {
      "label": "Saturday",
      "start": "2:00",
      "end": "3:00"
    },
    "sunday": {
      "label": "Sunday",
      "start": "2:00",
      "end": "3:00"
    }
  }
}

```


# 実行
## ログインを求められる場合があります
```
python3 matching.py
```
