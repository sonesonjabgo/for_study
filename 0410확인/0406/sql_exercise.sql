-- CRUD 
-- INSERT, SELECT, UPDATE, DELETE
-- INSERT INTO table_name (column1, column2, column3, ...)
--      VALUES (value1, value2, value3, ...) : 하나의 레코드 생성

-- 칼럼명 지정해서 해도되고
INSERT INTO emp (ename, job, sal)
      VALUES ('KIMSSAFY', 'PROGRAMMER', '6000');

-- 지정안해줄거면 컬럼 다 채워주고
INSERT INTO emp 
      VALUES ('7777','KIMSSAFY', 'PROGRAMMER', 7566, '6/4/2023', 6000, NULL, 20);

-- WHERE 지정해주지 않으면 전부가 대상
DELETE FROM emp;

-- 원하는 대상만 지우기
DELETE FROM emp WHERE ename = 'SCOTT';

-- UPDATE table_name
--    SET column name = value,
--        column name = value,
--        column name = value,
--        column name = value
--  WHERE 조건문 ...
UPDATE emp
  SET deptno = 50
  WHERE MGR = 7698;

UPDATE emp
  SET deptno = 30
  WHERE deptno = 50;

-- 전직원의 급여의 총합을 구하라
SELECT SUM(sal) AS '급여 총합'
  FROM emp;

-- 전 사원의 수를 구하라
SELECT COUNT(*) AS '사원 수'
  FROM emp;

-- 부서별 급여의 합
SELECT deptno, sum(sal) 
  FROM emp
  GROUP BY deptno;

-- 업무별 급여의 총합
SELECT job, sum(sal+IFNULL(comm,0)) AS '총합'
  FROM emp
  GROUP BY job;

-- 부서별 업무별 급여의 총합
SELECT deptno, job, sum(sal+IFNULL(comm,0)) 
  FROM emp
  GROUP BY deptno, job;

-- 자신의 업무별 급여의 평균보다 많이 받는 직원을 조회
SELECT empno, ename
  FROM emp e1
  WHERE e.sal > (SELECT avg(e2.sal+IFNULL(e2.comm,0))
                  FROM emp e2
                  WHERE e2.job = e1.job
                  GROUP BY e2.job);


SELECT avg(sal+IFNULL(comm,0)), job
  FROM emp
 -- WHERE job = 'SALESMAN'
  GROUP BY job;

-- JOIN 활용
-- 모든 직원의 사번, 이름, 부서번호, 부서 이름, 업무를 조회
SELECT empno, ename, deptno, job
  FROM emp;

SELECT deptno, DNAME
  FROM dept;

-- 이거시 JOIN
-- 카테시안 곱 사용
-- 동등조인, INNER JOIN
SELECT empno, ename, e.deptno, d.deptno, dname
  FROM emp e, dept d
  WHERE e.deptno = d.deptno;

-- 각 직원의 사번, 이름, 부서번호, 매니저 이름, 업무를 조회
-- 매니저 이름 >> 매니저 번호로 작성되어 있고 내가 참조해야 할 것이 내 자신의 key임
SELECT * FROM emp;

-- 셀프 조인
SELECT e1.empno, e1.ename, e1.deptno, e1.mgr, e2.ename as manager, e1.job
  FROM emp e1, emp e2
  -- emp 테이블 두개가 카테시안 곱을 만들어냄
  WHERE e1.mgr = e2.empno;

-- 부서에 직원이 없는 부서도 조회
-- OUTER JOIN 
SELECT empno, ename, e.deptno, d.deptno, dname
  FROM emp e RIGHT LEFT OUTER JOIN dept d
  WHERE e.deptno = d.deptno;