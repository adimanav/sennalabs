select * from 
(select user.name as name, count(user_car.userid) as num_cars from user_car
inner join user on user.id = user_car.userid
group by user.name)
where num_cars > 2