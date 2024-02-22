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


