# Web App

## Links

- [XD プロトタイプ](https://xd.adobe.com/view/00f5a7b2-4a01-4867-60f3-c4a10b1cb50a-76c4/)

## ルーティング

| ページ | ルーティング | Templateファイル |
| :---: | :---: | :---: |
| TOP(診断するページ) | / | index.html |
| Result | /result | result.html |

## About Develop

### 開発サーバーの起動

```shell script
$ cd path/to/image_recognition_app
$ python server.py
```

### ディレクトリ構成

- web_app
    - templates
        - base.html : 全てのtemplateファイルで継承するbase template
    - static
         - css
         - js
         - images
    - settigs.py : 各種設定情報を置く
- server.py : 開発サーバー起動用スクリプト
