CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
-- 테이블의 컬럼 수 5개는 잘 맞췄지만, 순서를 신경쓰지 않았다.
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

DELETE FROM zoo WHERE name = '5';

-- 수정
-- name, eat, weight, height, age
INSERT INTO zoo VALUES
('gorilla', 'omnivore', 180, 210, 5);

-- 2)
-- rowid가 중복으로 입력되어 있음
-- eligator의 rowid 수정
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(11, 'alligator', 'carnivore', 250, 50);

SELECT rowid, name FROM zoo;

-- 3)
-- weight는 NOT NULL이여서 값을 넣어줘야 한다
-- weight 도 지정해줌
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 300, 3);