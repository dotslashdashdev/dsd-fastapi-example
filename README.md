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
보통 Virtualenv라고 부르는 파이썬 가상 환경은 별도 구분된 디렉터리에 파이썬 인터프리터를 복제하고, `activate` 명령어를 제공함으로써 현재 터미널 세션만 파이썬 버전과 의존성 패키지들의 경로를 제한(Sandbox) 할 수 있습니다.  

Virtuanenv는 만드는 가장 기초적인 방법은 파이썬3에 내장된 `venv` 모듈을 이용하는 것 입니다.   
하지만 이 프로젝트에서는 더 나은 의존성 관리와 버전 관리(Lock)를 제공하는 Poetry를 사용합니다.  

> Poetry 설치하기
> https://python-poetry.org/docs/

Poetry가 설치 되었다면, 이 프로젝트의 의존성 패키지를 설치합니다.   

```
$ poetry install
```


## FastAPI 서버 실행
```
# 파이썬 가상환경이 활성화되어 있지 않을 때
# $ poetry shell

# 실행 환경을 구분하는 ENV_STATE 환경변수 선언
$ export ENV_STATE="local"

$ cd src
$ python main.py
```

서버가 정상적으로 실행되었다면, [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 접속해서 Swagger API 문서가 정상적으로 보이는 지 확인합니다.  


## 마무리
개발 마무리 단계에는 `formatting.sh` 파일을 실행하여 코드 포맷팅을 진행합니다.  

```
$ /bin/bash formatting.sh
```
