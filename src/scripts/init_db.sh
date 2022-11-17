# MySQL 실행 중인지 확인
# MySQL 임시 컨테이너 띄워서 SQL 실행
#  - users 테이블 생성
#  - users 시드 데이터 삽입

if [ "$(docker ps -q -f name=mysql8-example)" ]; then
  echo "MySQL 서버 컨테이너가 실행 중 입니다."
  MYSQL_RUNNING_PORT="$(docker port mysql8-example | cut -d ':' -f2)"
  if [ $MYSQL_RUNNING_PORT != "3306" ]; then
    echo "MySQL 서버가 3306 포트를 개방하고 있지 않습니다."
    exit 1
  else
    docker cp `pwd`/sql/. mysql8-example:/sql
    docker exec mysql8-example /bin/sh -c 'mysql -u root -ppassword! example < /sql/create_tables.sql'
    docker exec mysql8-example /bin/sh -c 'mysql -u root -ppassword! example < /sql/insert_users_data.sql'
    echo "테이블 생성 및 회원 정보 입력 완료"
  fi
else
  echo "실행 중인 MySQL 컨테이너를 찾을 수 없습니다."
fi