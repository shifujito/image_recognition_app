# image_recognition_app
# 環境構築
- conda create --name image-app python=3.6
- conda activate image-app
- conda install --file requirement.txt
## このアプリの作成理由
1. 居酒屋などの年齢確認とかにあったら便利だと思ったから
1. 老けている理由をヒートマップにより判断できると思ったから
## 概要
1. Flaskを使って画像認識アプリを作成する。
1. inputは画像,outputは認識したものとそれを選んだ根拠のヒートマップを出力する。
## fine-tuning
1. Xception
1. Inception V3
1. ResNet50
1,VGG16
1. VGG19
1. MobileNet
## deta水増し
3. 回転させたり
3. 引き延ばしたりする
## 画像のスクレイピング
2. https://www.talent-databank.co.jp/search/result?_t=20200518023853&_page=1&_view=list
2. 上記のurlから6000件のデータを取得
## Flaskによるwebアプリ化
1. まだ不明
