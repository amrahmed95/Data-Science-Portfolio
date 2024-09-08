WITH 
    -- Define variables as constants
    constants AS (
        SELECT 
            0.02 AS conversion_rate,     -- 2%
            5.00 AS product_cost,        -- $5.00 per product
            50000.00 AS campaign_cost    -- $50,000.00 campaign cost
    ),
    
    -- CTE for calculating and rounding the average views per video from the view_german_youtubers_2024
    rounded_views AS (
        SELECT 
            channel_name,
            subscribers, 
            ROUND(CAST(total_views AS numeric) / total_videos, -4) AS avg_views_per_video
        FROM view_german_youtubers_2024
        WHERE total_videos > 0  -- Ensure no division by zero
    )

-- Final SELECT query using constants and rounded average views per video
SELECT 
    r.channel_name,
    r.subscribers,  
    r.avg_views_per_video,
    (r.avg_views_per_video * c.conversion_rate) AS est_sales_per_video,
    (r.avg_views_per_video * c.conversion_rate * c.product_cost) AS est_revenue_per_video,
    ((r.avg_views_per_video * c.conversion_rate * c.product_cost) - c.campaign_cost) AS net_profit
FROM 
    rounded_views r, 
    constants c
ORDER BY 
    r.subscribers DESC 
LIMIT 5;
