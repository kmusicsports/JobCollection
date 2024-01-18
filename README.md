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
  - [アプリへのアクセス](#アプリへのアクセス)
  - [データベースへのアクセス](#データベースへのアクセス)
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

<details><summary>企業管理</summary>

```Mermaid
---
title: 企業管理
---
classDiagram
  class CompanyController {
    -CompanyService company_service
    +CompanyController(CompanyService company_service)
    +create() werkzeug.wrappers.response.Response
    +show_list() str
    +show_detail(int id) str
    +delete(int id) werkzeug.wrappers.response.Response
  }
  class CompanyService {
    +create(ImmutableMultiDict[str, str] form) str | None
    +make_list() list[CompanyName]
    +find(int id) CompanyName | None
    +delete(int id) str | None
  }
  class CompanyServiceImpl {
    -CompanyRepository company_repository
    +CompanyServiceImpl(CompanyRepository company_repository)
    +create(ImmutableMultiDict[str, str] form) str | None
    +make_list() list[CompanyName]
    +find(int id) CompanyName | None
    +delete(int id) str | None
  }
  class CompanyRepository {
    +create(Company company) Company | None
    +find(int id) Company | None
    +find_all() list[Company]
    +update(Company company) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyRepositoryImpl {
    +CompanyRepositoryImpl()
    +create(Company company) Company | None
    +find(int id) Company | None
    +find_all() list[Company]
    +update(Company company) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyName {
    -int id
    -str name
    +CompanyName()
    +CompanyName(Company company)
    +toEntity() Company
  }
  class Company {
    -int id
    -str name
    -str business
    -str mvv
    -str required_skill
    -str location
    -str benefit
    -str applying_motivation
    +Company(name)
    +Company(int id, str name, str business, str mvv, str required_skill, str location, str benefit, str applying_motivation)
    +get_id()
    +get_name()
    +get_business()
    +get_mvv()
    +get_required_skill()
    +get_location()
    +get_benefit()
    +get_applying_motivation()
  }
  <<interface>> CompanyRepository
  <<interface>> CompanyService
  CompanyController..>CompanyService : 依存
  CompanyService..|>CompanyServiceImpl : 実現
  CompanyServiceImpl..>CompanyRepository : 依存
  CompanyRepository..|>CompanyRepositoryImpl : 実現
  CompanyName--Company : 関連
  CompanyController--CompanyName : 関連
  CompanyService--CompanyName : 関連
  CompanyServiceImpl--CompanyName : 関連
  CompanyRepository--Company : 関連
  CompanyRepositoryImpl--Company : 関連
```

</details>

<details><summary>企業の基本情報管理</summary>

```Mermaid
---
title: 企業の基本情報管理
---
classDiagram
  class CompanyInfoController {
    -CompanyInfoService company_info_service
    +CompanyInfoController(CompanyInfoService company_info_service)
    +show(int id) str
    +update(ImmutableMultiDict[str, str] form) werkzeug.wrappers.response.Response
  }
  class CompanyInfoService {
    +find(int id) CompanyInfo | None
    +update(ImmutableMultiDict[str, str] form) str | None
  }
  class CompanyInfoServiceImpl {
    -CompanyRepository company_repository
    +CompanyInfoServiceImpl(CompanyRepository company_repository)
    +find(int id) CompanyInfo | None
    +update(ImmutableMultiDict[str, str] form) str | None
  }
  class CompanyRepository {
    +create(Company company) Company | None
    +find(int id) Company | None
    +find_all() list[Company]
    +update(Company company) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyRepositoryImpl {
    +CompanyRepositoryImpl()
    +create(Company company) Company | None
    +find(int id) Company | None
    +find_all() list[Company]
    +update(Company company) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyInfo {
    -int id
    -str name
    -str business
    -str mvv
    -str required_skill
    -str location
    -str benefit
    -str applying_motivation
    +CompanyInfo(Company company)
    +toEntity() Company
  }
  class Company {
    -int id
    -str name
    -str business
    -str mvv
    -str required_skill
    -str location
    -str benefit
    -str applying_motivation
    +Company(name)
    +Company(int id, str name, str business, str mvv, str required_skill, str location, str benefit, str applying_motivation)
    +get_id()
    +get_name()
    +get_business()
    +get_mvv()
    +get_required_skill()
    +get_location()
    +get_benefit()
    +get_applying_motivation()
  }
  <<interface>> CompanyRepository
  <<interface>> CompanyInfoService
  CompanyInfoController..>CompanyInfoService : 依存
  CompanyInfoService..|>CompanyInfoServiceImpl : 実現
  CompanyInfoServiceImpl..>CompanyRepository : 依存
  CompanyRepository..|>CompanyRepositoryImpl : 実現
  CompanyInfo--Company : 関連
  CompanyInfoController--CompanyInfo : 関連
  CompanyInfoService--CompanyInfo : 関連
  CompanyInfoServiceImpl--CompanyInfo : 関連
  CompanyRepository--Company : 関連
  CompanyRepositoryImpl--Company : 関連
```

</details>

<details><summary>企業との接触情報管理</summary>

```Mermaid
---
title: 企業との接触情報管理
---
classDiagram
  class CompanyConnectionController {
    -CompanyConnectionService company_connection_service
    +CompanyConnectionController(CompanyConnectionService company_connection_service)
    +create() werkzeug.wrappers.response.Response
    +show_list() str
    +update(ImmutableMultiDict[str, str] form) werkzeug.wrappers.response.Response
    +delete(int id) werkzeug.wrappers.response.Response
  }
  class CompanyConnectionService {
    +create(CompanyConnection company_connection) str | None
    +make_list() list[CompanyConnectionForm]
    +update(CompanyConnectionForm company_connection_form) str | None
    +delete(int id) str | None
  }
  class CompanyConnectionServiceImpl {
    -CompanyConnectionRepository company_connection_repository
    +CompanyConnectionServiceImpl(CompanyConnectionRepository company_connection_repository)
    +create(CompanyConnectionForm company_connection_form) str | None
    +make_list() list[CompanyConnectionForm]
    +update(CompanyConnectionForm company_connection_form) str | None
    +delete(int id) str | None
  }
  class CompanyConnectionRepository {
    +create(CompanyConnection company_connection) CompanyConnection | None
    +find_all() list[CompanyConnection]
    +update(CompanyConnection company_connection) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyConnectionRepositoryImpl {
    +CompanyConnectionRepositoryImpl()
    +create(CompanyConnection company_connection) CompanyConnection | None
    +find_all() list[CompanyConnection]
    +update(CompanyConnection company_connection) Exception | None
    +delete(int id) Exception | None
  }
  class CompanyConnectionForm {
    -int id
    -int company_id
    -date connection_date
    -str way
    -str employee
    -str content
    -str route
    -int company_id
    -date connection_date
    -str way
    -str employee
    -str content
    -str route
    +CompanyConnectionForm(company_id)
    +CompanyConnectionForm(CompanyConnection companyConnection)
    +toEntity() CompanyConnection
  }
  class CompanyConnection {
    -int id
    -int company_id
    -date connection_date
    -str way
    -str employee
    -str content
    -str route
    -int company_id
    -date connection_date
    -str way
    -str employee
    -str content
    -str route
    +CompanyConnection(int id, int company_id, date connection_date, str way, str employee, str content, str route, int company_id, date connection_date, str way, str employee, str content, str route)
    +get_id()
    +get_company_id()
    +get_connection_date()
    +get_way()
    +get_employee()
    +get_content()
    +get_route()
    +get_company_id()
    +get_connection_date()
    +get_way()
    +get_employee()
    +get_content()
    +get_route()
  }
  <<interface>> CompanyConnectionRepository
  <<interface>> CompanyConnectionService
  CompanyConnectionController..>CompanyConnectionService : 依存
  CompanyConnectionService..|>CompanyConnectionServiceImpl : 実現
  CompanyConnectionServiceImpl..>CompanyConnectionRepository : 依存
  CompanyConnectionRepository..|>CompanyConnectionRepositoryImpl : 実現
  CompanyConnectionController--CompanyConnectionForm : 関連
  CompanyConnectionService--CompanyConnectionForm : 関連
  CompanyConnectionServiceImpl--CompanyConnectionForm : 関連
  CompanyConnectionRepository--CompanyConnection : 関連
  CompanyConnectionRepositoryImpl--CompanyConnection : 関連
  CompanyConnectionForm--CompanyConnection : 関連
```

</details>

#### ER図

```Mermaid
erDiagram
  company {
    int id
    string name
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

<details><summary>company</summary>

| No | 論理名(カラム名) | 物理名(内容) | データ型 | PK | FK | Not Null | Default | Unique |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | id | 企業のID | INT | 〇 |  | 〇 | AUTO_INCREMENT |  |
| 2 | name | 企業名 | VARCHAR |  |  | 〇 |  |  |
| 3 | business | 業務内容 | TEXT |  |  |  |  |  |
| 4 | mvv | 経営理念 | TEXT |  |  |  |  |  |
| 5 | required_skill | 求められているスキル | TEXT |  |  |  |  |  |
| 6 | location | 勤務地(本社の所在地、支社など) | TEXT |  |  |  |  |  |
| 7 | benefit | 福利厚生・社内制度 | TEXT |  |  |  |  |  |
| 8 | applying_motivation | 志望動機 | TEXT |  |  |  |  |  |

</details>

<details><summary>company_connection</summary>

| No | 論理名(カラム名) | 物理名(内容) | データ型 | PK | FK | Not Null | Default | Unique |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | id | 接触情報のID | INT | 〇 |  | 〇 | AUTO_INCREMENT |  |
| 2 | company_id | 企業のID | INT |  | 〇 | 〇 |  | 〇 |
| 3 | company_date | 接触日時 | DATE |  |  | 〇 |  |  |
| 4 | way | 接触方法 | TEXT |  |  |  |  |  |
| 5 | employee | 担当者、接触した社員の情報 | TEXT |  |  |  |  |  |
| 6 | content | 内容 | TEXT |  |  | 〇 |  |  |
| 7 | route | 経由 | TEXT |  |  |  |  |  |

</details>

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
│   │   ├── entity                     テーブルと紐づくモデル
│   │   ├── model                      表示用のモデル
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
- Python 3.11
- VSCode拡張機能
  - Python
  - EditorConfig for VS Code

### ビルド＆起動

```bash
docker compose up
```

### アプリへのアクセス

起動が完了すると、アプリのURL[http://localhost:5001](http://localhost:5001)へアクセス可能になっています。

### データベースへのアクセス

1. docker compose execコマンドを打つと、サーバーに入れる。

    ```bash
    docker compose exec db bash
    ```

2. mysqlコマンドを打つと、パスワードの入力画面が表示される。

    ```bash
    mysql -u docker -p
    ```

3. パスワード「docker」を打つと、MySQL コマンドラインツールが起動し MySQL に接続します。

    ```bash
    Enter password: ******
    ```

### 停止＆破棄

```bash
docker compose down
```
