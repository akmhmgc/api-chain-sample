# FastAPI + APIChain sample

国と時間帯に基づいて挨拶を返す簡単なAPIサーバーをたてた上で、LangChainのAPIChainを使用することでAPIドキュメントを与えるだけで適切なAPIエンドポイントを叩くことができるサンプルです。

## 環境構築

まず、アプリケーションで必要なライブラリをインストールしてください。`requirements.txt`ファイルに記載されているライブラリをインストールするには、以下のコマンドを実行します。

```bash
pip install -r requirements.txt
```

## アプリケーションの実行

環境構築が完了したら、アプリケーションを実行することができます。次のコマンドを実行して、アプリケーションを起動してください。

```bash
uvicorn main:app --reload
```

このコマンドは、`main.py`ファイル内のFastAPIインスタンス`app`を使用して、アプリケーションを起動します。`--reload`オプションを使うことで、コードの変更が自動的に反映されるようになります。

## APIの利用

アプリケーションが起動している間は、以下のURLでAPIにアクセスできます。

```
http://127.0.0.1:8000
```

APIエンドポイントには、`time`（時間帯）と`country`（言語コード）パラメータが必要です。例えば、日本語の朝の挨拶を取得するには、以下のURLを使用します。

```
http://127.0.0.1:8000/?time=morning&country=ja
```

Webブラウザや`curl`コマンド、またはPostmanのようなAPIクライアントを使ってリクエストを送信し、挨拶を取得できます。

## APIChainを利用してAPIを叩く

```bash
export OPENAI_API_KEY=<your api key>
```

```bash
python langchain/api_chain.py
```

```output
Question: ドイツの朝の挨拶は？

> Entering new APIChain chain...
http://127.0.0.1:8000/?time=morning&country=de
{"greeting":"Guten Morgen"}

> Finished chain.
```

質問内容に合わせて適切にAPIエンドポイントを叩いてくれていることがわかります🎉
