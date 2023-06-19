# Anaconda Prompt (管理者モード) で以下のコマンド、Flaskをインストール　
conda install flask

# Anaconda Prompt (通常モード)で作業ディレクトリに移動
cd 自分の作業ディレクトリ
# 例えば、C:\Users\koyama\Documents\授業資料\第5回

# Flaskアプリを作るディレクトリを作成して移動
mkdir test_apps
cd test_apps

# app1.py を実装し、以下のコマンドで起動
flask --app app1 run
# Ctrl + C で立ち下げ

# app2.py を実装し、以下のコマンドで起動
flask --app app1 run
# Ctrl + C で立ち下げ
# 続いて、以下のコマンドで起動（デバッグモード）
flask --app app2 --debug run
# Ctrl + C で立ち下げ

# 以下、app3.py ~ app6.py をそれぞれ実装して、デバッグモードで動作確認

# app7.py は、以下のコマンドだけで起動可能
python3 app7.py