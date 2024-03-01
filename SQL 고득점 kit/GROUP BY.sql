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


