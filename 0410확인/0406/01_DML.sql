-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- users 테이블의 전체 행 수 조회
SELECT COUNT(*) FROM users;

-- 전체 유저의 평균 balance
SELECT avg(balance) FROM users;

-- 모든 유저의 지역 중복없이
SELECT DISTINCT country FROM users;

-- 전라북도의 평균
SELECT country, avg(balance) FROM users
WHERE country='전라북도';

-- 지역별 평균 밸런스
SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

-- 나이 30이상 평균 나이
SELECT avg(age) FROM users
WHERE age >= 30;

-- 각 지역별로 몇 명씩 살고 있는 지
SELECT country, COUNT(*) FROM users
GROUP BY country;

-- 각 성씨가 몇 명씩 있는지
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;

SELECT last_name, COUNT(*) AS number_of_name FROM users
GROUP BY last_name;

CREATE table classmates (
 name TEXT NOT NULL,
 age INTEGER NOT NULL,
 address TEXT NOT NULL
);

-- 단일 행 삽입
INSERT INTO classmates (name, age, address)
VALUES ('홍길동',23,'서울');

INSERT INTO classmates
VALUES ('홍길동',23,'서울');

-- 여러 행 삽입
INSERT INTO classmates
VALUES
 ('김철수',30,'경기'),
 ('이영미',31,'강원'),
 ('박진성',26,'전라'),
 ('최지수',12,'충청'),
 ('정요한',28,'경상');

-- 2번 데이터 이름을 '김철수한무두루미' 주소를 '제주도'로 수정
UPDATE classmates 
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;

-- 5번 데이터 삭제하기
DELETE FROM classmates WHERE rowid = 5;

-- 이름에 '영'이 포함되는 데이터 삭제
DELETE FROM classmates WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제
DELETE FROM classmates;

