select user.name, count(user_car.userid) from user_car
inner join user on user.id = user_car.userid
group by user.name