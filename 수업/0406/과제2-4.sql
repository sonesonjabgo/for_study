CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

-- 다섯 개의 컬럼을 가진 테이블을 만듭니다.
-- height, age 컬럼 외의 컬럼은 NULL 값이면 안됩니다.
-- 6개의 데이터를 INSERT ~ VALUE로 넣어줍니다.


-- 트랜잭션은 터미널에서 진행해야 합니다.
-- 트랜잭션의 종류인 BEGIN, ROLLBACK, COMMIT에 관한 문제입니다.
-- BEGIN을 통해 여러 단계의 처리의 시작점을 만들고
-- COMMIT은 최종적으로 데이터 베이스에 반영하는 것 이고
-- ROLLBACK은 실패하기 전 지점으로 돌아가게 하는 것 입니다.