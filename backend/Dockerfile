# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# 依存関係をコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install -r requirements.txt

# ソースコードをコピー
COPY . .

# Flaskアプリの起動
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--reload"]
