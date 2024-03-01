SELECT FOOD_TYPE, REST_ID, REST_NAME, favorites
FROM REST_INFO
WHERE (food_type, favorites) in ( -- 타입별 가장 높은 좋아요수인 컬럼 출력 -> 서브쿼리: 타입별 가장 높은 좋아요 + 인 컬럼 출력
    select food_type, max(favorites) -- 2. select에 명시 -> 3. 후 max, count 등
    from rest_info
    group by food_type -- 1. GROUP BY 로 묶는다면, 
)
order by FOOD_TYPE desc


SELECT name, count(*)
from ANIMAL_INS
where name is not null -- 이름이 없으면 집계 제외
group by name
having count(*) >= 2 -- Having 은 group에 대한 필터
order by name asc


SELECT hour(datetime) as hour, count(*) as count
from animal_outs
where hour(datetime) between 9 and 19 -- hour(datetime) = date_format(datetime, "%h") 와 같음
-- datetime이 9-19시 인거 필터링
group by hour(datetime) -- 9-19 각각 시간별로 그룹화
order by hour(datetime)


SELECT FLOOR((price/10000))*10000 as PRICE_GROUP, count(*) PRODUCTS
-- 내림 FLOOR, 올림 CEILING
-- truncate(price/10000, 0)*10000 0자리까지 잘라내기
-- 반올림 ROUND
FROM PRODUCT
GROUP BY PRICE_GROUP -- select에서 price_group이 정의되지만 group by 가능함. 
ORDER BY PRICE_GROUP


SELECT CAR_TYPE, COUNT(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS like "%통풍시트%" -- 포함 단어 다중 조건
or OPTIONS like "%열선시트%"
or OPTIONS like "%가죽시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE


SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID -- 그룹바이에 두개 이상의 컬럼 : 곱진법?
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC


SELECT CATEGORY, PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN -- 서브쿼리 + IN 같이 쓰기. MAX인 것이 아닌 MAX인 "것들"을 출력
   (SELECT CATEGORY, max(PRICE) AS PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY = '과자' or  CATEGORY = '국' or   CATEGORY = '김치'or CATEGORY = '식용유'  
    GROUP BY CATEGORY)
ORDER BY PRICE DESC;


SELECT CAR_ID, 
    MAX(CASE  -- 대여중과 대여 가능이 둘다 나올 수 있는 경우 MAX를 이용해 대여중이 나오도록 함
        WHEN date_format(start_date, "%Y-%m-%d") <= '2022-10-16' AND date_format(end_date, "%Y-%m-%d") >= '2022-10-16' THEN '대여중'
        ELSE '대여 가능'
    END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc


-- 상품을 구매한 회원 수 집계
SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, GENDER, COUNT(distinct i.USER_ID) USERS -- distinct로 중복 제거 후 집계
FROM USER_INFO as i, ONLINE_SALE as o
WHERE i.USER_ID = o.USER_ID
AND GENDER is not null
GROUP BY 1,2,3
ORDER BY 1,2,3


SELECT AUTHOR.AUTHOR_ID, AUTHOR.AUTHOR_NAME, CATEGORY ,sum(SALES * PRICE) as TOTAL_SALES -- sum(sales) * price가 아닌 sum(sales * price)로 해야함.
-- sum(sales)를 먼저 해버리는건 책마다 가격이 다르기 때문에 안됨
from BOOK, AUTHOR, BOOK_SALES
where BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID and BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
and SALES_DATE like '2022-01%'
group by CATEGORY, AUTHOR.AUTHOR_ID
order by AUTHOR_ID asc, CATEGORY desc


SELECT ID, name, host_id
from PLACES
WHERE HOST_ID in (SELECT HOST_ID  -- '헤비유저가 등록한' + '정보' => 서브쿼리
            FROM PLACES
            GROUP BY 1
            HAVING COUNT(HOST_ID)>=2)
order by id


SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt') -- 두개의 상품이 있는 카트만 출력
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2 -- 두개의 상품이 모두 있는 카트만 출력
ORDER BY CART_ID


