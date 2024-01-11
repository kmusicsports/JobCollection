# アプリ名

概要

## 目次 <!-- omit in toc -->

- [目的](#目的)
- [機能仕様](#機能仕様)
  - [企業管理機能](#企業管理機能)
    - [概要](#概要)
    - [構成機能](#構成機能)
    - [機能使用時の動画 or スクショ](#機能使用時の動画-or-スクショ)
  - [企業の基本情報管理機能](#企業の基本情報管理機能)
    - [概要](#概要-1)
    - [構成機能](#構成機能-1)
  - [機能使用時の動画 or スクショ](#機能使用時の動画-or-スクショ-1)
  - [企業との接触情報管理機能](#企業との接触情報管理機能)
    - [概要](#概要-2)
    - [構成機能](#構成機能-2)
    - [機能使用時の動画 or スクショ](#機能使用時の動画-or-スクショ-2)
  - [開発予定の機能一覧](#開発予定の機能一覧)
- [開発仕様](#開発仕様)
  - [設計資料](#設計資料)
    - [画面設計](#画面設計)
    - [クラス図](#クラス図)
    - [ER図](#er図)
    - [テーブル定義](#テーブル定義)
  - [使用技術](#使用技術)
  - [ソースコード構成](#ソースコード構成)
  - [セットアップ](#セットアップ)
  - [ビルド＆起動](#ビルド起動)
  - [停止＆破棄](#停止破棄)

## 目的

## 機能仕様

### 企業管理機能

#### 概要

企業(名)を登録し、登録した企業の基本情報の管理機能や企業との接触情報の管理機能が使えるようになります。

#### 構成機能

- 一覧表示
- 登録
- 削除
- 詳細表示

#### 機能使用時の動画 or スクショ

### 企業の基本情報管理機能

#### 概要

以下のような、企業の基本的な情報を管理することができます。

- 事業内容
- 経営理念・ミッション・バリュー・パーパス
- 求められるスキル
- 勤務地（本社の所在地、支社など）
- 福利厚生・社内制度
- 志望動機

#### 構成機能

- 表示
- 編集

### 機能使用時の動画 or スクショ

### 企業との接触情報管理機能

#### 概要

以下のように、企業と、いつ・どこで・だれと・どうやって接触し、何をしたのかという接触情報を管理することができます。

- 日付
- 接触方法（カジュアル面談、OB訪問、就活イベント、選考など）
- 担当者・接触した社員の情報
- 内容
- 経由（リクナビ、マイナビ、大学、研究室の教授など）

#### 構成機能

- 一覧表示
- 登録
- 編集
- 削除

#### 機能使用時の動画 or スクショ

### 開発予定の機能一覧

- 定形情報の管理機能（自己紹介、自己PR、ES、ガクチカなど）
- 求人情報の管理機能（職種、給与など）
- リンクの管理機能（公式HP、採用ページなど）
- 提出物の管理機能（ES、履歴書、コーディングテストなど）
- スケジュール管理機能（Googleカレンダー等の他アプリとの連携 or このアプリ内で完結）
- データ公開機能

## 開発仕様

### 設計資料

#### 画面設計

[https://www.notion.so/c83dad35885c4a7f8564cd325cf88105?pvs=4](https://www.notion.so/c83dad35885c4a7f8564cd325cf88105?pvs=4)
<!-- Figma URL（可能ならプロトタイプまで） -->

#### クラス図

```Mermaid
```

#### ER図

```Mermaid
erDiagram
  company ||--|| company_info : has
  company {
    int id
    string name
  }
  company_info {
    int id
    int company_id
    string business
    string mvv
    string required_skill
    string location
    string benefit
    string applying_motivation
  }
  company ||--o{ company_connection : has
  company_connection {
    int id
    int company_id
    date connection_date
    string way
    string employee
    string content
    string route
  }
```

#### テーブル定義

- company
  | No | 論理名(カラム名) | 物理名(内容) | データ型 | PK | FK | Not Null | Default | Unique |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  |  |  |  |  |  |  |  |  |  |
- company_info
  | No | 論理名(カラム名) | 物理名(内容) | データ型 | PK | FK | Not Null | Default | Unique |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  |  |  |  |  |  |  |  |  |  |
- company_connection
  | No | 論理名(カラム名) | 物理名(内容) | データ型 | PK | FK | Not Null | Default | Unique |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  |  |  |  |  |  |  |  |  |  |

### 使用技術

- Bootstrap
- Python
- Flask
- MySQL
- Docker, Docker Compose
- Git, GitHub

### ソースコード構成

```bash
アプリ名
├── db                                 データベース関連
│   ├── Dockerfile                     MySQL用Docker設定ファイル
│   ├── data                           MySQLのデータ
│   ├── initdb                         コンテナ起動時に実行するSQLファイル群
│   │   ├── 1_schema.sql               テーブル作成用SQLファイル
│   │   └── 2_data.sql                 初期データ登録用SQLファイル
│   └── my.cnf                         MySQL設定ファイル
├── docs                               ドキュメント関連
│   └── pull_request_template.md       プルリクエストのテンプレートファイル
│   python                             Python関連
│   ├── app                            アプリ関連
│   │   ├── controller                 制御、リクエストマッピング
│   │   ├── model                      Entity・Form・DTO、データとロジック（エンタープライズビジネスルール）
│   │   ├── repository                 データ操作
│   │   ├── service                    ビジネスロジック（アプリケーションビジネスルール）
│   │   ├── static                     静的ファイル群
│   │   │   ├── css                    CSSファイル郡
│   │   │   └── js                     JavaScriptファイル群
│   │   ├── templates                  HTMLファイル郡
│   │   │   ├── ・・・
│   │   │   └── base.html              全HTMLのベースになるHTML
│   │   └── application.py             初期設定（Flaskインスタンス、DBなど）
│   ├── Dockerfile                     Python用Docker設定ファイル
│   └── requirements.txt               pipパッケージ一覧
├── .editorconfig                      コーディングスタイル設定ファイル
├── .gitignore                         Git管理除外対象の設定ファイル
├── docker-compose.yml                 Docker Compose設定ファイル
└── README.md                          ドキュメント
```

### セットアップ

<!-- #### 前提条件 -->

- [Docker, Docker Compose](https://www.docker.com/)
- VSCode拡張機能（どれかが不要になるかも）
  - Remote Development
  - Python
  - EditorConfig for VS Code

### ビルド＆起動

```bash
docker compose up
```

### 停止＆破棄

```bash
docker compose down
```
