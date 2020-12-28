/*
Создайте хранимую функцию hello(),
которая будет возвращать приветствие, в зависимости от текущего времени суток.
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро",
с 12:00 до 18:00 функция должна возвращать фразу "Добрый день",
с 18:00 до 00:00 — "Добрый вечер",
с 00:00 до 6:00 — "Доброй ночи".
*/

delimiter //
create function hello()
returns varchar(255)
deterministic
begin
declare hour int;
set hour = hour(now());
	case
		when hour between 6 and 11 then
        return 'Good morning';
        when hour between 12 and 17 then
        return 'Good day';
        when hour between 18 and 23 then
        return 'Good evening';
        else
        return 'Good night';
	end case;
end//
delimiter ;

select hello()