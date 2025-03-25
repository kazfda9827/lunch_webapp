目標
1.fastapiで画像アップロード機能のついたwebアプリを作成する
2.dockerでコンテナイメージ作成・共有

ライブラリ
uvicorn                 0.32.0
fastapi                 0.115.4
Jinja2                  3.1.4
python-multipart        0.0.20

フォルダ説明
app　作業ディレクトリ
templates　フロントエンド部分？
files　アップロードした画像が保存される場所

動作確認方法 
1. git clone https://github.com/kazfda9827/lunch_webapp
2. pip install uvicorn fastapi　Jinja2　python-multipart
3. uvicorn main:app --reload
4. http://127.0.0.1:8000にアクセスする
5.画像をアップロードして、filesフォルダに保存されているか確認する
