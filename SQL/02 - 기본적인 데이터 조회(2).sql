/*dd
제목: 데이터 기본 조회(2)
작성: 이장래
내용: 기본적인 데이터 조회 방법 학습
*/

USE hrdb2024;
SELECT DATABASE();

/*
7. 범위 조건과 리스트 조건
*/

-- 급여가 5,000~8,000 사이인 직원 정보 조회
SELECT emp_name, emp_id, dept_id, hire_date, phone, salary
	FROM employee
	WHERE salary BETWEEN 5000 AND 8000;  # 5000이상 8000 이하이다. Python과 다르게 SQL은 미만, 초과 설정 불가

SELECT emp_name, emp_id, dept_id, hire_date, phone, salary
	FROM employee
	WHERE salary < 5000 OR salary > 8000;  # 반대 

SELECT emp_name, emp_id, dept_id, hire_date, phone, salary
	FROM employee
	WHERE salary NOT BETWEEN 5000 AND 8000;  # 이것도 가능 
    
-- SYS, MKT, GEN 부서 직원 정보 조회
SELECT emp_name, emp_id, dept_id, hire_date, phone
	FROM employee
	WHERE dept_id IN ('SYS', 'MKT', 'GEN');  # 해당 열 이외는 NOT IN 사용
# df['dept_id'].isin(['SYS', 'MKT', 'GEN'])  파이썬은 not in 안 됨..
-- 2020년에 입사한 직원 정보 조회
SELECT emp_name, emp_id, dept_id, hire_date, phone
	FROM employee
	WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31';


-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
-- Q) 2019년도에 입사한 정보시스템, 영업팀 직원 정보 조회
SELECT * FROM employee WHERE hire_date BETWEEN '2019-01-01' AND '2019-12-31' AND dept_id = 'SYS';


-- Q) 2019년도에 입사한 연봉이 6,000 이상인 근무중인 직원 정보 조회
SELECT * FROM employee WHERE hire_date BETWEEN '2019-01-01' AND '2019-12-31' AND salary >= 6000;


-- Q) 홍길동(S0001), 강우동(S0003), 오삼식(S0005)의 2019년 휴가 정보 조회
SELECT * FROM vacation WHERE emp_id IN ('S0001', 'S0003', 'S0005');


-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
 
/*
8. NULL 값 비교
*/

-- 근무 중인 직원 정보 조회 (?)
SELECT emp_name, emp_id, gender, dept_id, hire_date, retire_date, phone
	FROM employee
	WHERE retire_date = 'NULL';  # 'NULL' 이라는 문자열을 찾는 것임, 날짜형 데이터형에 문자열을 넣으므로 에러 발생

-- 근무 중인 직원 정보 조회 (?)
SELECT emp_name, emp_id, gender, dept_id, hire_date, phone
	FROM employee
	WHERE retire_date = NULL;  # 이렇게도 사용할 수 없다. 해당 열에 NULL이 아닌 값들만 존재하기 떄문에 무엇이 NULL인지 알 수 없음 

-- 근무 중인 직원 정보 조회 (!)
SELECT emp_name, emp_id, gender, dept_id, hire_date, retire_date, phone
	FROM employee
	WHERE retire_date IS NULL;
    
-- 퇴사한 직원 정보 조회
SELECT emp_name, emp_id, gender, dept_id, hire_date, retire_date, phone
	FROM employee
	WHERE retire_date IS NOT NULL;


-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
-- Q) 본부에 속하지 않은 부서 정보 조회



-- Q) 영어 이름이 없는 근무 중인 직원 정보 조회



-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --


/*
9. IFNULL() 함수
*/

-- IFNULL 함수 사용 전
SELECT emp_name, emp_id, eng_name, gender, dept_id, hire_date, phone
	FROM employee
	WHERE retire_date IS NULL;

-- IFNULL 함수 사용: eng_name 열 값이 NULL이면 공백 표시
SELECT emp_name, emp_id, IFNULL(eng_name, ''), gender, dept_id, hire_date, phone
	FROM employee
	WHERE retire_date IS NULL;

-- ORACLE에서는 ''값을 NULL로 취급
-- IFNULL 함수 결과에 별칭 사용
SELECT emp_name, emp_id, IFNULL(eng_name, '') AS eng_name, gender, dept_id, hire_date
	FROM employee
	WHERE retire_date IS NULL;

-- 참고: NULL값 처리 함수
-- MySQL: IFNULL()
-- ORACLE: NVL()
-- MSSQL: ISNULL()
-- 헐!! MySQL의 ISNULL() 함수는 NULL이면 1, 아니면 0

-- 모든 DBMS가 동시에 가지고 있는 함수, NULL 처리 함수가 너무 다르기 떄문에 COALESCE를 대체로 사용하는 것이 낫다.
-- COALESCE() 함수 사용 : 첫 번째로 NULL이 아닌 값을 반환
-- EX) COALESCE(NULL, NULL, NULL, 10, 20) --> 10
-- EX) COALESCE(NULL, 10) --> 10
-- EX) IFNULL(NULL, 10) --> 10 : IFNULL은 두 개의 값만 사용된다. 
-- 아래 예시는 열에있는 각 행마다 NULL이면 다음 값인 ''을 넣는다. 
SELECT emp_name, emp_id, COALESCE(eng_name, '') AS eng_name, gender, dept_id, hire_date
	FROM employee
	WHERE retire_date IS NULL;


-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --

-- Q) retire_date 열 값이 NULL이면 9999-12-31로 표시해서 직원 정보 조회



-- Q) salary열 값이 NULL이면 0으로 표시해서 근무 중인 여직원 정보 조회


    
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --


/*
9. 자동 형 변환
*/

-- 자동 형 변환
SELECT '10' + '20'; -- MySQL 30, ORACLE 30, MSSQL '1020'
SELECT 10 + '20'; -- 30
SELECT 10 + '20AX'; -- MySQL 30, ORACLE 10, MSSQL Error
SELECT 10 + 'LX20'; -- 10 + 0'
SELECT 'ABC' + 'DEF'; -- 0, MySQL은 문자열을 결합하지 못한다.
-- MySQL은 문자열을 숫자로 못바꾸면 0, 하지만 최대한 숫자로 바꾸려고 한다.

-- 문자열 데이터 결합
SELECT CONCAT('10', '20');
SELECT CONCAT(10, '20');
SELECT CONCAT(10, 20);
SELECT CONCAT(10, NULL); -- MySQL NULL, ORACLE 10..

-- 참고: 문자열 결합 연산
-- ORACLE: 'ABC' || 'DEF' || 'GHI' --> 'ABCDEFGHI'
-- MSSQL: 'ABC' + 'DEF' + 'GHI' --> 'ABCDEFGHI'
-- ORACLE: CONCAT('A', 'B', 'C') --> ERROR, 오라클은 두 개만 결합할 수 있음 ㅠ;
-- MSSQL: CONCAT('A', 'B', 'C') --> 'ABC'
/*
10. 데이터 결합
*/

SELECT CONCAT(emp_name, '(', emp_id, ')') AS emp_name, dept_id, gender, hire_date, email
	FROM employee
	WHERE retire_date IS NULL;

-- 문자와 숫자 결합
SELECT CONCAT(emp_name, '(', salary, ')') AS emp_name, dept_id, gender, hire_date, email
	FROM employee
	WHERE retire_date IS NULL;

-- 문자와 날짜 결합
SELECT CONCAT(emp_name, '(', hire_date, ')') AS emp_name, dept_id, gender, hire_date, email
	FROM employee
	WHERE retire_date IS NULL;

-- NULL과 결합하면?
SELECT CONCAT(emp_name, '(', eng_name, ')') AS emp_name, dept_id, gender, hire_date, email
	FROM employee
	WHERE retire_date IS NULL;

-- NULL 값 처리 #1
SELECT CONCAT(emp_name, '(', IFNULL(eng_name, ''), ')') AS emp_name, dept_id, gender, 
       hire_date, email
	FROM employee
	WHERE retire_date IS NULL;

-- NULL 값 처리 #2
SELECT CONCAT(emp_name, IFNULL(CONCAT('(', eng_name, ')'), '')) AS emp_name, dept_id, gender, 
       hire_date, email
	FROM employee
	WHERE retire_date IS NULL;
    

-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
-- Q) 사원번호와 부서코드를 묶어서(예: S0001(SYS)) 근무 중인 직원 정보 조회


 
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
  
    
/*
11. 데이터 정렬
*/

-- 오름차순: 1, 2, 3, 4 (ASC)
-- 내림차순: 4, 3, 2, 1 (DESC)

-- 이름을 기준으로 오름차순 정렬
SELECT emp_name, emp_id, gender, dept_id, hire_date, phone
	FROM employee
	WHERE retire_date IS NULL
	ORDER BY emp_name ASC;

-- 이름을 기준으로 내림차순 정렬
SELECT emp_name, emp_id, gender, dept_id, hire_date, phone
	FROM employee
	WHERE retire_date IS NULL
	ORDER BY emp_name DESC;

-- 부서코드를 기준으로 오름차순, 이름을 기준으로 내림차순 정렬
SELECT dept_id, emp_name, emp_id, gender, hire_date, phone
	FROM employee
	WHERE retire_date IS NULL
	ORDER BY dept_id ASC, emp_name DESC;  # id로 ASC 정렬 후 같은 id끼리는 이름으로 DESC

-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
-- Q) 연봉이 높은 순으로 정렬해서 근무 중인 직원 정보 조회
SELECT * 
	FROM employee 
    WHERE retire_date IS NULL
    ORDER BY salary DESC;

-- Q) 최근 입사자가 먼저 조회되도록 정렬해서 근무 중인 직원 정보 조회


    
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
 
  
/*
12. CASE 문
*/

-- 직원 정보 조회
SELECT emp_name, emp_id, gender, hire_date, salary
	FROM employee;

-- 성별: M, F --> 남자, 여자
SELECT emp_name, emp_id, 
       CASE WHEN gender = 'M' THEN '남자'
            WHEN gender = 'F' THEN '여자'
            ELSE '' END AS gender, 
	   hire_date, retire_date, salary
	FROM employee;

-- 다른 방법(추천하지 않음): gender='M' AND city='서울' 같은 중복 조건을 줄 수 없기 떄문
SELECT emp_name, emp_id, 
       CASE gender WHEN 'M' THEN '남자'
                   WHEN 'F' THEN '여자'
                   ELSE '' END AS gender, 
	   hire_date, retire_date, salary
	FROM employee;
    
-- 근무 상태를 근무, 퇴사로 표시
SELECT emp_name, emp_id, gender, hire_date, salary,
       CASE WHEN retire_date IS NULL THEN '근무'
            ELSE '퇴사' END AS status
	FROM employee;


-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --

-- Q) 부서 코드가 SYS이면 전화번호를 공백으로 해서 근무 중인 직원 조회


    
-- Q) 급여 크기를 상, 중, 하로 구분해서 근무 중인 직원 조회


    
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --
     
     
/*
13. IF 함수
: CASE 문은 너무 길다..
*/

-- 성별: M, F --> 남자, 여자 (단, gender 열에 M, F 만 입력 된다고 가정함)
SELECT emp_name, emp_id, 
       IF(gender = 'M', '남자', '여자') AS gender, 
	   hire_date, retire_date, salary
	FROM employee;

-- 성별: M, F --> 남자, 여자 (IF 함수 중첩해서 사용)
SELECT emp_name, emp_id, 
       IF(gender = 'M', '남자', IF(gender = 'F', '여자', '')) AS gender, 
	   hire_date, retire_date, salary
	FROM employee;
    
-- 근무 상태를 근무, 퇴사로 표시
SELECT emp_name, emp_id, gender, hire_date, salary,
       IF(retire_date IS NULL,  '근무', '퇴사') AS status
	FROM employee;

-- 영어 이름이 NULL이면 공백 표시
-- IFNULL(eng_name, '') AS eng_name 쓰면 더 단순해짐
-- 모든 함수는 상황에 따라 적절히 사용될 수 있음
SELECT emp_name, emp_id, 
       IF(eng_name IS NULL, '', eng_name) AS eng_name,
       gender, hire_date, salary
	FROM employee;

-- 참고: 최적의 쿼리로 데이터 프레임을 뷰로 만들어놓고 다른 사람들은 뷰를 가져다가 사용하면 된다.
CREATE VIEW emp_info
AS
SELECT emp_name, IFNULL(eng_name, '') AS eng_name, gender, hire_date, salary
	FROM employee;

-- 뷰 사용
SELECT * FROM emp_info;
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --

-- Q) 부서 코드가 SYS이면 전화번호를 공백으로 해서 근무 중인 직원 조회

    
    
-- Q) 급여 크기를 상, 중, 하로 구분해서 근무 중인 직원 조회


    
-- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * -- * --   