/*

# Data Cleaning steps

1. Remove unnecessary columns by only selecting the needed columns
2. Extract the youtube channel names from the first column
3. Rename the column names

*/

SELECT 
	channel_name
	subscribers, 
	total_views, 
	total_videos 
FROM german_yt
LIMIT 10


SELECT 
	name, 
	POSITION('@' IN name) AS Indexx
FROM german_yt


SELECT
    name,
    POSITION('@' IN name) AS Index,
    CAST(SUBSTRING(name, 1, POSITION('@' IN name) - 1) AS VARCHAR(100)) AS German_youtube_Channel
FROM german_yt;


SELECT
    -- name,
    -- POSITION('@' IN name) AS Index,
    CAST(SUBSTRING(name, 1, POSITION('@' IN name) - 1) AS VARCHAR(100)) AS top_German_youtubers,
	subscribers, 
	total_views, 
	total_videos 
FROM german_yt;

------------------------------------------------

DROP VIEW IF EXISTS view_german_youtubers_2024;


CREATE VIEW view_german_youtubers_2024 
AS
SELECT DISTINCT
    CAST(SUBSTRING(name, 1, POSITION('@' IN name) - 1) AS VARCHAR(100)) AS channel_name,
    CASE 
        WHEN subscribers ~ '^[0-9]+$' THEN CAST(subscribers AS BIGINT)
        ELSE NULL
    END AS subscribers,
    CASE 
        WHEN total_views ~ '^[0-9]+$' THEN CAST(total_views AS BIGINT)
        ELSE NULL
    END AS total_views,
    CASE 
        WHEN total_videos ~ '^[0-9]+$' THEN CAST(total_videos AS BIGINT)
        ELSE NULL
    END AS total_videos
FROM german_yt;



