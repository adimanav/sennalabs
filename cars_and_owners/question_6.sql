select user.name, car.name from user_car
inner join user on user.id = user_car.userid
inner join car on car.id = user_car.carid