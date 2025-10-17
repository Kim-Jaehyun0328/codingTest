-- 코드를 입력하세요
SELECT P.product_id, P.product_name, SUM(O.AMOUNT*P.price) as sum
from FOOD_PRODUCT P, FOOD_ORDER O
where P.PRODUCT_ID = O.PRODUCT_ID
and produce_date like '2022-05%'
group by product_id
order by sum desc, product_id asc
