import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # 標準設定ファイル読み込み
    app.config.from_object("settings")

    # 非公開設定ファイル読み込み
    if app.config["ENV"] == "development":
        app.config.from_pyfile(os.path.join("config", "development.py"), silent=True)
    else:
        app.config.from_pyfile(os.path.join("config", "production.py"), silent=True)

    if test_config is not None:
        # テスト用設定を上書き
        app.config.from_mapping(test_config)

    from .views.greeting import greeting

    app.register_blueprint(greeting, url_prefix="/greeting")

    return app
