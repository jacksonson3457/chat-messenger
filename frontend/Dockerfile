# ベースイメージ
FROM node:20-alpine

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY package*.json ./
RUN npm install

# ソースコードのコピー
COPY . .

# 開発サーバーを起動
EXPOSE 3000
CMD ["npm", "start"]
