-- Операторы
-- Task 1
update users set
	created_at = now() where created_at is null;
update users set
	updated_at = now() where updated_at is null;