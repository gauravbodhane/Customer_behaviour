-- Active: 1772962231314@@127.0.0.1@3306@test
-- Active: 1772962231314@@127.0.0.1@3306@gauravbd
select * from customers_cleaned ;
-- Q1. what is the total revenue genrated by male vs female customers?
select gender ,sum(purchase_amount) as revenue
from customers_cleaned
group by gender ;

-- Q2.which customer used a discount but still spend more thant the average purchase amount?
select customer_id ,purchase_amount 
from customers_cleaned
where discount_applied ='Yes' and purchase_amount >= (select AVG(purchase_amount) from customers_cleaned)
limit 40;

-- Q3. Which are the top 5 products with the highest
-- average review rating?
select item_purchased,round(avg(review_rating),2) as "Average Product Rating"
from customers_cleaned
group by item_purchased
order by avg(review_rating) desc
limit 5 ;

-- Q4.Compare the average purchase amount between standard and express shipping.
select shipping_type,
avg(purchase_amount)
from customers_cleaned
where shipping_type in ('Standard' ,'Express')
group by shipping_type;

-- Q5.Do subscribe, customers spread more? compare average spend and total revenue between 
-- subscribers and non-subscribers.
select subscription_status,
count(customer_id) as total_customers,
round(avg(purchase_amount),2) as  avg_spend,
round(sum(purchase_amount),2) as total_revenue
from customers_cleaned
group by subscription_status
order by total_revenue,avg_spend desc;

-- Q6.Which five products have the highest percentage of purchase with discount applied?
select item_purchased,
round(100*sum(case when discount_applied = 'Yes' then 1 else 0 end)/count(*),2) as discount_rate
from customers_cleaned
group by item_purchased
order by discount_rate desc
limit 5;

-- Q7.segment customer into new, returning, and loyal based on their total number
-- of previous purchase and show the count of each segment?
with customer_type as (
select customer_id,previous_purchases,
case
      when previous_purchases = 1 then 'New'
      when previous_purchases between 2 and 10 then 'Returning'
      Else 'Loyal'
      end as customer_segment
from customers_cleaned
)
select customer_segment, count(*) as "Number Of Customers"
from  customer_type
group by customer_segment ;

-- Q8.What are the top 3 most purchased products within each category?
-- i use here windows function 

with item_counts as (
select category,
item_purchased,
count(customer_id) as total_orders,
-- here i use row_number because in output there is number of output then the dense_rank
-- can put into same position hence i use row_number.
ROW_NUMBER()  over (partition by category order by count(customer_id) desc) as item_rank
from customers_cleaned
group by  category,item_purchased
)
select item_rank, category,item_purchased,total_orders
from item_counts
where item_rank <= 3;

-- Q9.Our customers who are repeat buyers (more than five previous purchases )also like to subscribe?
select subscription_status,
count(customer_id) as repeat_buyers
from customers_cleaned
where previous_purchases > 5
group by subscription_status;

-- Q10. what is the revenue contribute of each age group?
select age_group,
sum(purchase_amount) as total_revenue
from customers_cleaned
group by age_group 
order by total_revenue desc;


















