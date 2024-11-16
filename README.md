
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
      "times": [{ "start": "", "end": "" }]
    },
    "tuesday": {
      "label": "Tuesday",
      "times": [{ "start": "", "end": "" }]
    },
    "wednesday": {
      "label": "Wednesday",
      "times": [{ "start": "", "end": "" }]
    },
    "thursday": {
      "label": "Thursday",
      "times": [{ "start": "", "end": "" }]
    },
    "friday": {
      "label": "Friday",
      "times": [{ "start": "", "end": "" }]
    },
    "saturday": {
      "label": "Saturday",
      "times": [{ "start": "", "end": "" }]
    },
    "sunday": {
      "label": "Sunday",
      "times": [
        { "start": "2:00", "end": "3:00" },
        { "start": "3:15", "end": "4:30" },
        { "start": "4:45", "end": "6:00" }
      ]
    }
  }
}

```


# 実行
## ログインを求められる場合があります
```
python3 matching.py
```
