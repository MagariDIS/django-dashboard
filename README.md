# Django Dashboard Demo apps  [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)]()

 ![version](https://img.shields.io/badge/version-0.0.1-blue.svg)

![Material Dashboard Django - Admin Dashboard coded in Django.](https://github.com/creativetimofficial/material-dashboard-django/blob/master/media/material-dashboard-django-intro.gif)

<br />

> Free product の **Django Dashboard** を自習用に変更しています

- [dependencies](./requirements.txt): **Django 3.2.6 LTS**
- [SCSS compilation](#recompile-css) via **Gulp**
- UI Kit: **Material Dashboard** (Free Version) を使用 provided by **[Creative-Tim](https://www.creative-tim.com/)**
- SQLite Database
- Docker-compose Base 

<br />

## Table of Contents

* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Github](#GIT)
* [Resources](#resources)
* [Useful Links](#useful-links)

<br />


## Quick start

> mofficialのmaterial-dashboard-django.gitを編集していますので、正しくはオリジナルを参照してください

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/material-dashboard-django.git
$ cd material-dashboard-django
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## Documentation
 **Material Dashboard Django** のドキュメントは [website](https://demos.creative-tim.com/material-dashboard-django/docs/1.0/getting-started/getting-started-django.html)を参照ください。



<br />

## File Structure


```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br /> 

---

## Deployment

### [Docker](https://www.docker.com/) execution

> Note: ローカルにpython環境を作らず WLS2上のdocker-composeで開発しています 

```sh

docker-compose run appseed-app python manage.py startapp chat
docker-compose run appseed-app python manage.py migrate
```


The steps:

> Get the code

```bash
$ git clone https://github.com/creativetimofficial/material-dashboard-django.git
$ cd material-dashboard-django
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />


## Mange command:


> 不要なdocker imageの整理

```sh
docker-compose down --rmi all --volumes --remove-orphans

docker ps -a
docker image prune
```

<br />


```
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```


## Resources

GMAP API: AIzaSyAKWigPZLVTsdMGT3G34CirjBLcQ-mnf7c

## WLS2 仮想ディスクの圧縮方法

```
PS C:\WINDOWS\system32> cd ${HOME}\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\

ディレクトリ: ${HOME}\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState
Name
2022/02/08     17:55     9616490496 ext4.vhdx

Optimize-VHD -Path .\ext4.vhdx -Mode full  
```
- Documentation: <https://demos.creative-tim.com/material-dashboard-django/docs/1.0/getting-started/getting-started-django.html>

<br />

## TEST Codeing sample

改造例

![](modifyDashbordData2022-02-08.png)




<br />

# Git[](https://tutorial.django-dashboard.org/ja/deploy/#git)

## Gitリポジトリを始める

Gitはコードリポジトリ（または略して「リポジトリ」）というものの中に置かれる特定のファイルへの変更を追跡します。 私たちのプロジェクトを開始しましょう。 あなたのコンソールを開き、`django-dashboard` ディレクトリでこれらのコマンドを実行します。

> **備考：**リポジトリを初期化する前に `pwd` (OSX/Linux) または `cd` (Windows) コマンドで現在の作業ディレクトリを確認してください。 `django-dashboard` フォルダー内にいる必要があります。

command-line

```
$ git init
Initialized empty Git repository in ~/django-dashboard/.git/
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
```

gitリポジトリを初期化することは、プロジェクトごとに1回だけ行う必要があります（ユーザー名と電子メールをもう一度入力する必要はありません）。

Git はこのディレクトリ内のすべてのファイルとフォルダの変更を追跡しますが、無視してほしいいくつかのファイルがあります。 ベースディレクトリ内で `.gitignore` という名前のファイルを作成することによってこれを行います。 あなたのエディターを開き、次の内容で新しいファイルを作成します。

.gitignore

```
*.pyc
*~
/.vscode
__pycache__
myvenv
db.sqlite3
/static
.DS_Store
```

これを "django-dashboard" フォルダ内に `.gitignore` という名前で保存します。

> **備考：**ファイル名の先頭のドットは重要です! もしそのファイルを作るのが難しいなら、（Macをお使いの方はFinderからドット（ . ）で始まるファイルを作れません。）そういう時はエディタでSave Asから作成すれば問題ありません。 `.txt`や `.py`などの拡張子をファイル名に入れないように気をつけてください。 ファイル名が`.gitignore`でないとGitに認識されません。
> 
> **備考：** `.gitignore`ファイルで指定したファイルの1つが`db.sqlite3`です。 そのファイルはローカルデータベースで、すべてのユーザーと投稿が保存されます。 私達は標準的なウェブプログラミングの慣習に従います。つまり、ローカルのテストサイトとPythonAnywhere上の本番のウェブサイトでデータベースを分けるということです。 PythonAnywhereのデータベースは開発用のマシンと同じようにSQLiteにすることができますが、通常はMySQLというSQLiteよりもたくさんのサイト訪問者に対処できるデータベースを使用します。 どちらの方法でも、GitHubのコードのコピーではSQLiteデータベースを無視することで、これまでに作成したすべての投稿と管理者はそのままローカルで利用できますが、本番環境（ブログを公開するPythonAnywhereのことです）ではそれらを再び作成する必要があります。 ローカルデータベースは本当のブログ投稿をブログから削除してしまうことを心配せずに、さまざまなことをテストできるよい遊び場として考えるといいでしょう。

`git add` コマンドを実行する前や、どのような変更を加えたか定かでない時は、 `git status` コマンドを使用する事をおすすめします。 これは間違ったファイルを追加またはコミットなど思いもかけない事を止めるために役立ちます。 `git status` コマンドは、あらゆる追跡されていない/変更されている/ステージされている（untracked/modifed/staged）ファイルや、ブランチの状態などさまざまな情報を返します。 出力は次のようになります。

command-line

```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .gitignore
        blog/
        manage.py
        mysite/
        requirements.txt

nothing added to commit but untracked files present (use "git add" to track)
```

最後に、変更内容を保存します。コンソールに移動し、これらのコマンドを実行します。

command-line

```
$ git add --all .
$ git commit -m "My Django Girls app, first commit"
 [...]
 13 files changed, 200 insertions(+)
 create mode 100644 .gitignore
 [...]
 create mode 100644 mysite/wsgi.py
```

## GitHubにコードをプッシュする[](https://tutorial.django-dashboard.org/ja/deploy/#github%E3%81%AB%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E3%83%97%E3%83%83%E3%82%B7%E3%83%A5%E3%81%99%E3%82%8B)

[GitHub.com](https://www.github.com/)にアクセスし、Sign upをクリックして無料の新規アカウントを作成してください。 （ワークショップの前にすでに作成していたら、それは素晴らしいです!） あなたのパスワードを忘れないようにしてください（使っていたら、パスワードマネージャーに入れておいてください）

そして、新しいリポジトリに "django-dashboard"の名前で新しいリポジトリを作成します。 "READMEで初期化する"チェックボックスをオフのままにし、.gitignoreオプションを空白にして（手動で行っています）、ライセンスをNoneのままにしておきます。

![](images/new_github_repo.png)

> **注** `django-dashboard`という名前は重要です。何か他のものを選択することもできますが、以下の手順では何度も繰り返す必要があります。他の名前を選択した場合は、 毎回それを置き換えてください。 できれば、`django-dashboard` の名前にしておきましょう。

次の画面では、リポジトリをクローンするためのURLが表示されます。これはこの後のコマンドで利用します。

![](images/github_get_repo_url_screenshot.png)

そして自分のコンピューター上のGitリポジトリをGitHub上のGitリポジトリに結びつけてあげる必要があります。

コンソールに次のように入力します（`<your-github-username>`をGitHubアカウントの作成時に入力したユーザー名に置き換えます。山カッコ<>を残さないでください。このURLはさっき見たクローンURLと一致する必要があります）。

command-line

```
$ git remote add origin https://github.com/<your-github-username>/django-dashboard.git
$ git push -u origin master
```

GitHubにプッシュするとき、GitHubのユーザー名とパスワードを聞かれます（コマンドライン上かポップアップウィンドウにて）。認証情報を入力したらこんな風に表示されます。

command-line

```
Counting objects: 6, done.
Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)

To https://github.com/ola/django-dashboard.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

あなたのコードは今GitHub上にあります。 
<br />

## Useful Links

- [More products](https://www.creative-tim.com/bootstrap-themes) from Creative Tim
- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Freebies](https://www.creative-tim.com/bootstrap-themes/free) from Creative Tim
- [Affiliate Program](https://www.creative-tim.com/affiliates/new) (earn money)

<br />

## Social Media

- Twitter: <https://twitter.com/CreativeTim>
- Facebook: <https://www.facebook.com/CreativeTim>
- Dribbble: <https://dribbble.com/creativetim>
- Instagram: <https://www.instagram.com/CreativeTimOfficial>

<br />

---
[Material Dashboard Django](https://www.creative-tim.com/product/material-dashboard-django) - Provided by [Creative Tim](https://www.creative-tim.com/) and [AppSeed](https://appseed.us)
