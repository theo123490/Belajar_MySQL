-- SET SQL_SAFE_UPDATES = 0;

-- UPDATE item_list
-- SET item_type = REPLACE(item_type,'Spectroscopy','S') 
-- WHERE item_type = 'Spectroscopy'

-- SELECT * FROM type_list

-- ALTER TABLE lab_assistant ADD CONSTRAINT FOREIGN KEY (specialty) REFERENCES type_list (type_code);

SELECT *
FROM item_list
	inner join item_list.item_type on type_list.item_type
WHERE type_list.type_desc = "Fiber%123%Optic"

-- FETCH ONE (SELECT specialty FROM lab_assistant WHERE asst_name = "Theodore")



