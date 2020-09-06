# flask-skeleton

Python 用 Web アプリケーションフレームワーク "Flask" の用途別ディレクトリ構成スケルトン

## flask-web-proto

Module 版 Flask アプリケーション

### 用途

- Web アプリケーションのプロトタイプ
- 小規模 Web アプリケーション

### 設定ファイル

| ファイルパス                                   | 設定内容       |        |
| :--------------------------------------------- | :------------- | :----- |
| flask-web-proto/settings.py                    | 標準設定       | 公開   |
| flask-web-proto/instance/config/development.py | 開発環境用設定 | 非公開 |
| flask-web-proto/instance/config/production.py  | 本番環境用設定 | 非公開 |

※ instance ディレクトリ内は Git の追跡対象外なので、別途作成が必要

### 開発サーバ起動

```
$ export FLASK_APP=application.py
$ export FLASK_ENV=development
$ flask run
```

### デバッグ用 URL

`http://localhost:5000/Hi?user_name=hrgm`

## flask-web-app

Package 版 Flask アプリケーション

### 用途

- 中規模 Web アプリケーション

大規模な Web アプリケーションを構築する場合は、 Django などのフルスタック Web アプリケーションフレームワークを使用した方がいいかも…

### 設定ファイル

| ファイルパス                                 | 設定内容       |        |
| :------------------------------------------- | :------------- | :----- |
| flask-web-app/settings.py                    | 標準設定       | 公開   |
| flask-web-app/instance/config/development.py | 開発環境用設定 | 非公開 |
| flask-web-app/instance/config/production.py  | 本番環境用設定 | 非公開 |

※ instance ディレクトリ内は Git の追跡対象外なので、別途作成が必要

### 開発サーバ起動

```
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

### デバッグ用 URL

`http://localhost:5000/greeting/Hi?user_name=hrgm`

## flask-rest-api

RESTful API (REST API) Flask アプリケーション

### 用途

- RESTful API (REST API)

### 設定ファイル

| ファイルパス                                  | 設定内容       |        |
| :-------------------------------------------- | :------------- | :----- |
| flask-rest-api/settings.py                    | 標準設定       | 公開   |
| flask-rest-api/instance/config/development.py | 開発環境用設定 | 非公開 |
| flask-rest-api/instance/config/production.py  | 本番環境用設定 | 非公開 |

※ instance ディレクトリ内は Git の追跡対象外なので、別途作成が必要

### 開発サーバ起動

```
$ export FLASK_APP=api
$ export FLASK_ENV=development
$ flask run
```

### デバッグ用 URL

`http://localhost:5000/greeting/Hi?user_name=hrgm`
