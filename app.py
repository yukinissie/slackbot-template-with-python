# 環境変数を.envファイルからでも用意できるように
from dotenv import load_dotenv
load_dotenv()
# App本体
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# ここから下に何らかの処理を書く

# 例：helloと送ったらHello, world! @送信者名!と返す
@app.message("hello")
def message_hello(message, say):
    say(f"Hello, world! <@{message['user']}>!")


# ここから上に何らかの処理を書く

# HTTPサーバーとして起動
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
