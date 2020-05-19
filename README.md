# image_recognition_app
# 環境構築
- conda create --name image-app python=3.6
- conda activate image-app
- conda install --file requirement.txt
## このアプリの作成理由
## 概要
1. Flaskを使って画像認識アプリを作成する。
1. inputは画像,outputは認識したものとそれを選んだ根拠のヒートマップを出力する。
# 学習方法
```shell script
$ python train.py -e 12 -b 128
```

## 学習済みモデルを使って予測する
```shell script
$ python predict.py
```

## Flaskによるwebアプリ化

詳細は, [web_app/README](/web_app/README.md) に.
