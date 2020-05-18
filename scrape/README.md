# データスクレイピング

```shell script
$ python collect-data.py 
```

## 初期設定

settings.py の `CHROME_DRIVER_PATH` を自分用の設定で上書きする

~~あとでちゃんと環境変数からとれるようにします...~~

## カスタマイズ

``` python:collect_data.py
if __name__ == '__main__':
    Main(browser=False, init_id=105).run()
```

`init_id` に 初期IDを渡す.

既存の最大値を渡す必要あり.

### その他

`settings.TIME_SPAN`,  `collect_data.py` の `browser` 辺り.
