# Python Log Monitor Tool

## 概要

Python Log Monitor Tool は、ログファイルから `WARNING` と `ERROR` を含む行を抽出し、重要なログだけを別ファイルに保存するツールです。

また、WARNING件数、ERROR件数、合計件数、状態を JSON ファイルとして出力します。

このツールは、インフラ運用で行う「ログ確認」「異常検知」「障害調査の初期対応」をイメージして作成しました。

---

## 作った理由

AWS や Linux の学習を進める中で、サーバー運用ではログ確認が重要だと学びました。

実務では、Webサーバーやアプリケーションのログを確認し、エラーや警告を見つける場面があります。

そこで、Python を使ってログを読み取り、重要な情報だけを抽出する練習として、このツールを作成しました。

---

## できること

- `app.log` を読み込む
- `WARNING` を含む行を抽出する
- `ERROR` を含む行を抽出する
- 抽出した重要ログを `important.log` に保存する
- WARNING件数を数える
- ERROR件数を数える
- 合計件数を数える
- 結果を `important_summary.json` に保存する
- Python自身の実行ログを `script.log` に保存する

---

## 使用技術

- Python 3
- Linux
- EC2
- JSON
- ファイル操作
- 条件分岐
- ループ処理
- 関数

---

## ファイル構成

```text
python-log-monitor-tool/
├── monitor.py
├── app.log
├── important.log
├── important_summary.json
├── script.log
└── README.md
```

---

## 各ファイルの役割

| ファイル名 | 役割 |
|---|---|
| `monitor.py` | メインのPythonプログラム |
| `app.log` | 読み込む元のログファイル |
| `important.log` | WARNING / ERROR を抽出した結果 |
| `important_summary.json` | 件数や状態をまとめたJSONファイル |
| `script.log` | Pythonプログラム自身の実行ログ |
| `README.md` | このツールの説明書 |

---

## 使い方

### 1. Pythonファイルを実行する

```bash
python3 monitor.py
```

このコマンドは、`monitor.py` というPythonプログラムを実行します。

---

### 2. 抽出結果を確認する

```bash
cat important.log
```

このコマンドは、抽出された WARNING / ERROR のログを表示します。

---

### 3. 集計結果を確認する

```bash
cat important_summary.json
```

このコマンドは、WARNING件数、ERROR件数、合計件数、状態を表示します。

---

### 4. 実行ログを確認する

```bash
cat script.log
```

このコマンドは、Pythonプログラムがいつ実行されたかなどを確認するために使います。

---
## 実行例

以下のコマンドでツールを実行します。

```bash
python3 monitor.py
```

実行結果:

```text
Log monitoring completed.
WARNING: 2
ERROR: 2
STATUS: NG
```

この結果から、`app.log` の中に WARNING が2件、ERROR が2件あり、ERROR が存在するためステータスは `NG` と判定されます。

---
## 出力例

### important.log

```text
WARNING Disk usage is high
ERROR Failed to connect to database
WARNING Memory usage is high
ERROR Timeout occurred
```

### important_summary.json

```json
{
    "warning_count": 2,
    "error_count": 2,
    "total_important_count": 4,
    "status": "NG"
}
```

---

## 実務でのイメージ

このツールは、インフラ運用で行うログ確認の基本に近いです。

たとえば、Webサーバーやアプリケーションサーバーで障害が起きたとき、エンジニアはログを確認します。

大量のログの中から、`ERROR` や `WARNING` を見つけることで、問題の原因を探しやすくなります。

このツールでは、その作業をPythonで自動化する練習をしています。

---

## 学んだこと

このツールを作る中で、以下を学びました。

- ファイルを開いて読み込む方法
- 条件に合う行だけを抽出する方法
- 件数をカウントする方法
- JSON形式で結果を保存する方法
- Pythonプログラム自身の実行ログを残す方法
- ログ監視の基本的な考え方

---

## 今後の改善

今後は、以下の機能を追加したいです。

- ログファイル名をコマンドライン引数で指定できるようにする
- `CRITICAL` など他のログレベルにも対応する
- エラー率を計算する
- 一定以上のエラーが出たらアラートを出す
- AWS CloudWatch Logs のような監視サービスとの違いを整理する

---

## まとめ

このツールは、Pythonの基礎文法を使って、インフラ運用で重要なログ確認を自動化するために作成しました。

単なる文法練習ではなく、実務で使われる「ログを見る」「異常を見つける」「結果を記録する」という流れを意識しています。
