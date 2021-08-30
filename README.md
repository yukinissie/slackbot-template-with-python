# slackbot-template-with-python
以下を参考にします。

https://slack.dev/bolt-python/ja-jp/tutorial/getting-started

## 環境
```
python -V
# Python 3.9.0

ngrok -v
# ngrok version 2.3.40

sw_vers
# ProductName:    macOS
# ProductVersion: 11.2.3
# BuildVersion:   20D91
```

## install
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```

## 開発開始時にすること
```
source .venv/bin/activate
python app.py
ngrok http 3000
```

## 開発終了時にすること
```
Botを終了(ctrl+c)
ngrokを終了(ctrl+c)
deactivate
```

## herokuにデプロイ
### ログイン
```
heroku login
```

### herokuアプリの作成

```
heroku create <app-name>
```

### herokuに環境変数を設定
```
heroku config:set SLACK_SIGNING_SECRET=<your-signing-secret>
heroku config:set SLACK_BOT_TOKEN=xoxb-<your-bot-token>
```

### herokuにデプロイ
```
git push heroku main
```