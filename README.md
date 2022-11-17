DotSlashDash FastAPI Example
----

## 필수 요구 사항
- Python3.9
- Poetry
- Docker
- MySql


## 로컬 DB 실행
```
$ docker run -d --name mysql8-example \
  -v {로컬 디렉터리}/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=password! \
  -e MYSQL_DATABASE=example \ 
  -e MYSQL_USER=sample_user \
  -e MYSQL_PASSWORD='SamP!2U5er' \
  -p 3306:3306 \
  mysql:8
```

## 로컬 DB 테이블 생성 및 회원 데이터 세팅
```
$ cd src/scripts
$ /bin/bash init_db.sh
```


## 파이썬 개발 환경
```
$ poetry install
```


## FastAPI 서버 실행
```
$ poetry shell
$ cd src
$ python main.py
```