SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
CASE
WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여' -- datediff(end, start) 는 end - start
ELSE '단기 대여'
END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
ORDER BY HISTORY_ID DESC;



SELECT CAR_ID, ROUND(AVG(datediff(end_date, start_date)+1), 1) as AVERAGE_DURATION -- round는 반올림. truncate는 내림
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, car_id desc


SELECT substring(PRODUCT_CODE, 1, 2) as CATEGORY, count(*) -- substring 문자열 슬라이싱
from PRODUCT
group by substring(PRODUCT_CODE, 1, 2)


SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, "%Y-%m-%d") as out_date,
    case
    when out_date is null then '출고미정' -- =null 안됨 . is null
    when date_format(out_date, "%m-%d") <= "05-01" then '출고완료'
    else '출고대기'
    end as '출고여부'
from FOOD_ORDER
order by order_id


SELECT USER_ID, NICKNAME, concat(city, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소,  -- substring, concat 활용
concat(substring(tlno, 1, 3), '-', substring(tlno, 4, 4), '-', substring(tlno, 8, 4)) as 전화번호
from USED_GOODS_USER, USED_GOODS_BOARD
where USED_GOODS_USER.USER_ID = USED_GOODS_BOARD.WRITER_ID
group by USER_ID
having count(USER_ID) >= 3
order by USER_ID desc


