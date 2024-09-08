/*

# Data quality tests
-----------------------
1. Data needs to be 200 records of Youtube channels (Row Count test) 	-- PASSED!
2. Data needs 4 fields (Column Count test )							-- PASSED!
3. Check Column types 													-- PASSED!
	-- Channel Name: String
	-- Other columns: numerical data type
4. Each record is unique with (Duplicate count check)	-- PASSED!


* Row count - 200
* Column count - 4

DataTypes
----------
Channel_name = VARCHAR
subscribers = INTEGER
total_views = INTEGER
total_videos = INTEGER

Duplicate count = 0

*/



-- 1. Row Count Test:

SELECT COUNT(*) AS numberOfRows
FROM view_german_youtubers_2024;


-- 2. Column Count Test:

SELECT COUNT(*) AS column_count
FROM information_schema.columns
WHERE table_name = 'view_german_youtubers_2024'


-- 3. Check Column Types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'view_german_youtubers_2024'


-- 4. Duplicate Count Check

SELECT channel_name, COUNT(*) AS duplicate_count 
FROM view_german_youtubers_2024
GROUP BY channel_name
HAVING COUNT(*) > 1;


-- Check for Null Values -- 

SELECT 
    COUNT(*) FILTER (WHERE subscribers IS NULL) AS null_subscribers,
    COUNT(*) FILTER (WHERE total_views IS NULL) AS null_total_views,
    COUNT(*) FILTER (WHERE total_videos IS NULL) AS null_total_videos
FROM view_german_youtubers_2024;


