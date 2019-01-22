# 190122 수업정리

### 1. chat.py (c9)

- file read & write

```
- file에서 answer에 입력한 답이 기록된 횟수를 같이 print한다.
- 입력된 시간을 초단위까지와 몇번째 입력된 데이터인지 print한다.
- 소문자로만 입력받는다.
- feeling에 디폴트값을 soso 로 준다.
- 함수화한다.

# id, feeling, timestamp
# 1, good, 2019012209291123
# 2, bad, 2019012209300122
# 3, happy, 20190122305302

# create(input("What's up?: "))
# read(id=1)
# update(id=1, feeling='bad')
# delete(id=1)
```



### 2. SQL -structed query language

- q는 쿼리 Query 

질문!?

특수목적의 프로그래밍 언어

SQL로 데이터베이스를 관리함



- database DB

영구적인 데이터 저장을 위해 만들어짐

체계화된 데이터의 집합



- RDBMS

관계형 모델을 기반으로 하는 데이터베이스 관리 시스템

대표적인 오픈소스 RDBMS(MySQL, SQLite, PostgreSQL), ORACLE, MS SQL이다.

Not file!! but Program!!!!!

서버를 가지고 독립적인 작동함

본격적으로 사용할땐 MySQL이나 ORACLE주로 사용

 - 우리가 쓸 것은 SQLite !!

   파일 하나만 존재! 서버가 아닌 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스.

   기능을 많이 떼어내고 경량화를 택함.

   구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스



- 스키마 scheme

데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조

각 컬럼에 들어올 자료형을 정해놓는것.

데이터베이스의 구조와 제약조건에 대해 ...

컬럼과 데이터타입은 항상 정의하고 어떻게 만들지 고민 => 데이터베이스 모델링을 한다!

데이터레코딩, 테이블 만들기

절대 중복되지 않으면서 유니크한 데이터를  id로하며, 보통 1, 2, 3..으로 작성함.

데이터를 쓰고 확정되어 써넣고 저장되는 순간 id가 자동할당됨

ex)` id(INT)`,  `feeling(STRING)`, `timestamp(DATETIME)`



- 

c9에서 터미널에  sqlite3 입력

;이 찍혀야 쿼리가 끝났다는 것을 인식함

명령어는 대문자로!

.으로 시작하는 명령어는 SQLite프로그램 전용 명령어라 ;안써도 됨



맨처음 스키마 설정함



- 

```
Table 생성 (Datatype: INTEGER, TEXT)

CREATE TABLE <table_name> (
	<col1> DATATYPE,
	<col2> DATATYPE,
	...
	);
	
Data 입력
INSERT INTO <table_name> (<col1>, <col2>, ..)
VALUES (<data1>, <data2>, ... );

data전체 조회
SELECT * FROM <table_name>;
```

```
ex)
CREATE TABLE menus (
	id INTEGER,
	menu1 TEXT,
	menu2 TEXT
	);
	
INSERT INTO menus (id, menu1, menu2)
VALUES (1, 'Pho', 'Pork');

SELECT * FROM menus;
```



- 

my_db.sqlite3 만들어 sqlite3 my_db.sqlite3로 실행하면 입력한 내용이 휘발되지 않고 저장됨

table/ 내용 중 어떤 것을 어떻게 다루는지 차이를 알기!



.mode csv => csv모드로 보겠다!

.mode column => 컬럼모드로 보겠다.

.import user.csv users => user.csv를 users에 넣어준다

SELECT * FROM users



table이름 바꾸는 방법

ALTER TABLE users RENAME TO userssss

.table로 확인해보면 users 가 userssss로 바뀌어 있는 것을 확인할 수 있다.

DROP TABLE <table_name) 하면 지우기



https://zzu.li/hellodb 로 가서 users.csv 저장하여 이용

```
# create_table.sql로 저장

CREATE TABLE users(
	id INT PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	age INT,
	country TEXT,
	phone TEXT,
	balence INT
	);
```

.read create_table.sql 하면 테이블 만들어짐

.import users.csv users



SELECT * FROM users WHERE id=100;

=> id가 100인 사람들

SELECT * FROM users WHERE id>100;

=> id가 100 초과인 사람들



- Validation

id INT PRIMARY KEY NOT NULL => 비워놓을 수 없는 정보, 안써넣음 오류남.

유효성검사를 한다 == 밸리데이션을 건다

데이터가 데이터베이스에 들어갈 때 유효한지 아닌지를 검사한다.



- 

id INT PRIMARY KEY AUTOINCREMENT 자동으로 하나씩 올라감 INT형 자료에서만 사용가능







# SQL 정리

## SQLite3 전용 명령어

| 명령어                             | 설명                                        |
| ---------------------------------- | ------------------------------------------- |
| `.mode csv`                        | csv 처럼 보임                               |
| `.mode column`                     | 컬럼 기준으로 보임                          |
| `.headers on`                      | 헤더(컬럼이름)같이 출력                     |
| `.real <file.sql>`                 | 해당 sql                                    |
| `.import <file.name> <table_name>` | 해당 파일의 데이터를 지정한 테이블에 import |
| `.schema`                          | 스키마 전체 보기                            |



## TABLE 조작 관련

### Table생성 

```plsql
CREATE TABLE <table_name> (
	<col> DATA_TYPE PRIMARY KEY AUTOINCREMENT,
	<col> DATA_TYPE NOT NULL,
    <col> DATA_TYPE,
    ..
);
```



### Table (+ 레코드 모두) 삭제

```plsql
DROP TABLE <table_names>;
```



### Table 이름 수정

```plsql
ALTER TABLE <table_name>
RENAME TO <new_table_name>;
```

#### 

### Table 컬럼 추가



## Data 조작 관련

### Data 생성 (Create)

```plsql
INSERT INTO <table_name> (<col_name1>,         <col_name2>, ...)
VALUES
(<value_1>, <value_2>, ....),
(<value_1>, <value_2>, ....),
...
(<value_1>, <value_2>, ....);
```



### Data 조회 (Read, Retrieve)

#### 테이블에서 데이터 전체를 모든 col에 대하여 조회

```plsql
SELECT * FROM <table_name>;
```

#### 테이블에서 특정 컬럼만 조회

```plsql
SELECT <col_1>, <col_2>, ...  FROM <table_name>;
```

#### 테이블 조건으로 전체 컬럼 조회

```plsql
SELECT * FROM <table_name> WHERE [condition];
```



### Data 수정 (Update)

```plsql
UPDATE <table_name>
SET <col_1>=<val_1>, <col_2>=<val_2>, ...
WHERE [condition]; --보통 primary key (id) 로 선택
```



### Data 삭제 (Delete, Destroy)

```plsql
DELETE FROM <table_name>
WHERE [condition]; --보통 primary key (id) 로 선택
```

=> CRUD operation이라고 한다.



## Expression

###  해당 컬럼의 갯수

```sql
SELECT COUNT(<col_1>) FROM <table_name>;
```



### 해당 컬럼의

```sql
--평균
SELECT AVG(<col>) FROM <table_name>;
--총합
SELECT SUM(<col>) FROM <table_name>;
--최소
SELECT MIN(<col>) FROM <table_name>;
--최대
SELECT MAX(<col>) FROM <table_name>;
```



## 정렬(order)

```sql
SELECT <col> FROM <table_name>
ORDER BY <col_1>, <col_2> [ASC | DESC];
```

ASC : 오름차순 

DESC: 내림차순

## 제한(Limit)

```sql
SELECT <col> FROM <table_name>
LIMIT <num>;
```

num만큼만!

## 패턴(Pattern)

```sql
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>';
```

| 시작 | 예시      | 설명                                  |
| ---- | --------- | ------------------------------------- |
| %    | 2%        | 2로 시작하는 말                       |
|      | %2        | 2로 끝나는 말                         |
|      | %2%       | 2가 들어가는 값                       |
| _    | _2        | 두번째 글자가 2인 값                  |
|      | 1___      | 1로 시작하는 네자리 글자              |
|      | _2%       | 한글자 뒤에 2가 오고 뒤에 이어지는 값 |
|      | 2 _ % _ % | 2로 시작하는데 최소 3자리인 값        |

