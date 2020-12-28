/*
В таблице products есть два текстовых поля:
name с названием товара и description с его описанием.
Допустимо присутствие обоих полей или одно из них.
Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема.
Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены.
При попытке присвоить полям NULL-значение необходимо отменить операцию.
*/

delimiter //
CREATE TRIGGER trig BEFORE INSERT ON shop.products
FOR EACH ROW
BEGIN
	case
		when (NEW.name is null AND NEW.desription is null) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Are u ofigel? No NULL mf!';
		when NEW.name is null THEN
			SET NEW.name = 'undefined';
		when NEW.desription is null THEN
			SET NEW.desription = 'undefined';
	end case;
END //
delimiter ;