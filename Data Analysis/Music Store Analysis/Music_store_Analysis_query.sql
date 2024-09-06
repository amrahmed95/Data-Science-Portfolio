-- 1. Who is the senior most employee based on job title?
SELECT first_name, last_name, title
FROM public.employee
ORDER BY title DESC
LIMIT 1;

-- 2. Which countries have the most Invoices?
SELECT billing_country, COUNT(invoice_id) AS invoice_count
FROM Invoice
GROUP BY billing_country
ORDER BY invoice_count DESC;

-- 3. What are top 3 values of total invoice?
SELECT invoice_id, total
FROM Invoice
ORDER BY total DESC
LIMIT 3;


-- 4. Which city has the best customers? We would like to throw a promotional Music Festival in the city we made the most money. 
	-- Write a query that returns one city that has the highest sum of invoice totals. Return both the city name & sum of all invoice totals

SELECT 
	billing_city AS City,
	SUM(total) AS total_revenue	
FROM Invoice
GROUP BY billing_city
ORDER BY total_revenue DESC
LIMIT 10;


-- 5. Who is the best customers? The customer who has spent the most money will be declared the best customer. 
	--Write a query that returns the person who has spent the most money
SELECT 
	c.first_name,
	c.last_name,
	c.email,
	SUM(i.total) AS total_spent
FROM customer c
JOIN Invoice i
	ON c.customer_id = i.customer_id
GROUP BY
	c.customer_id
ORDER BY total_spent DESC
LIMIT 10;


-- 6. Write query to return the email, first name, last name, & Genre of all Rock Music listeners. 
	-- Return your list ordered alphabetically by email starting with A	
	-- [Email, first name, last name, & Genre of all Rock Music listeners]
SELECT 
	c.email,
	c.first_name,
	c.last_name,
	g.name AS genre
FROM customer c 
JOIN invoice i ON c.customer_id = i.customer_id
JOIN Invoice_line iL ON i.invoice_id = il.invoice_id
JOIN Track t ON il.track_id = t.track_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
ORDER BY c.email;


-- 6. Let's invite the artists who have written the most rock music in our dataset. 
	-- Write a query that returns the Artist name and total track count of the top 10 rock bands
	-- [Top 10 rock bands with the most tracks]:
	
SELECT 
	a.name AS artist_name, 
	COUNT(t.track_id) AS track_count
FROM artist a
JOIN album al ON a.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
GROUP BY a.artist_id, a.name
ORDER BY track_count DESC
LIMIT 10;


-- 7. Return all the track names that have a song length longer than the average song length. 
	-- Return the Name and Milliseconds for each track. Order by the song length with the longest songs listed first
	-- [Tracks longer than the average song length]

WITH avg_length AS (
  SELECT AVG(milliseconds) AS avg_milliseconds
  FROM track
)
SELECT 
	name, 
	milliseconds
FROM track, avg_length
WHERE milliseconds > avg_length.avg_milliseconds
ORDER BY milliseconds DESC;

-- 8. Find how much amount spent by each customer on artists? 
	-- Return customer name, artist name and total spent
		--[Amount spent by each customer on artists:]

WITH best_selling_artist AS (
	SELECT artist.artist_id AS artist_id, artist.name AS artist_name, SUM(invoice_line.unit_price*invoice_line.quantity) AS total_sales
	FROM invoice_line
	JOIN track ON track.track_id = invoice_line.track_id
	JOIN album ON album.album_id = track.album_id
	JOIN artist ON artist.artist_id = album.artist_id
	GROUP BY 1
	ORDER BY 3 DESC
	LIMIT 1
)
SELECT c.customer_id, c.first_name, c.last_name, bsa.artist_name, SUM(il.unit_price*il.quantity) AS amount_spent
FROM invoice i
JOIN customer c ON c.customer_id = i.customer_id
JOIN invoice_line il ON il.invoice_id = i.invoice_id
JOIN track t ON t.track_id = il.track_id
JOIN album alb ON alb.album_id = t.album_id
JOIN best_selling_artist bsa ON bsa.artist_id = alb.artist_id
GROUP BY 1,2,3,4
ORDER BY 5 DESC;


-- 9. We want to find out the most popular music Genre for each country. 
-- 	We determine the most popular genre as the genre with the highest amount of purchases. 
-- Returns each country along with the top Genre. For countries where the maximum number of purchases is shared return all Genres
-- [ Most popular genre for each country ]	

----------------------
-- Recursive_CTE --
----------------------

WITH genre_sales AS (
  SELECT 
  	i.billing_country AS country, 
	g.name AS genre, 
	SUM(il.unit_price * il.quantity) AS total_sales
  FROM invoice i
  JOIN invoice_line il ON i.invoice_id = il.invoice_id
  JOIN track t ON il.track_id = t.track_id
  JOIN genre g ON t.genre_id = g.genre_id
  GROUP BY i.billing_country, g.name
),
max_sales AS (
  SELECT country, MAX(total_sales) AS max_sales
  FROM genre_sales
  GROUP BY country
)

SELECT gs.country, gs.genre
FROM genre_sales gs
JOIN max_sales ms 
	ON gs.country = ms.country 
		AND gs.total_sales = ms.max_sales;



-- 10.Find the customer that has spent the most on music for each country. 
	-- Returns the country along with the top customer and how much they spent. 
	-- For countries where the top amount spent is shared, provide all customers who spent this amount
	-- [Customer that has spent the most on music for each country]
	
WITH customer_spending AS (
  SELECT 
  	i.billing_country AS country, 
	c.first_name, 
	c.last_name, 
	SUM(il.unit_price * il.quantity) AS total_spent
  FROM invoice i
  JOIN customer c ON i.customer_id = c.customer_id
  JOIN invoice_line il ON i.invoice_id = il.invoice_id
  GROUP BY i.billing_country, c.customer_id
),
max_spending AS (
  SELECT country, MAX(total_spent) AS max_spent
  FROM customer_spending
  GROUP BY country
)

SELECT cs.country, cs.first_name, cs.last_name, cs.total_spent
FROM customer_spending cs
JOIN max_spending ms 
	ON cs.country = ms.country 
		AND cs.total_spent = ms.max_spent;



----------------------------------------------------------------------
-- More Analysis Questions
----------------------------------------------------------------------
-- 1. Track and Sales Analysis:
---------------------------------------------
-- Which tracks generate the highest revenue?

SELECT 
	t.name AS track_name,
	SUM(il.unit_price * il.quantity) AS total_revenue
FROMtrack t
JOINinvoice_line il ON t.track_id = il.track_id
GROUP BY t.track_id
ORDER BY total_revenue DESC
LIMIT 10;


-- How do sales vary by genre or media type?
SELECT 
	g.name AS genre, 
	mt.name AS media_type, 
	SUM(il.unit_price * il.quantity) AS total_sales
FROMtrack t
JOINgenre g ON t.genre_id = g.genre_id
JOINmedia_type mt ON t.media_type_id = mt.media_type_id
JOINinvoice_line il ON t.track_id = il.track_id
GROUP BY g.name, mt.name
ORDER BY total_sales DESC;

-- What is the average price per track, and how does it differ across genres or albums?

	-- Average price per track by genre
	SELECT 
		g.name AS genre, 
		AVG(t.unit_price) AS avg_price
	FROM track t
	JOIN genre g 
		ON t.genre_id = g.genre_id
	GROUP BY g.name
	ORDER BY avg_price DESC;
	
	-- Average price per track by album
	SELECT 
		al.title AS album, 
		AVG(t.unit_price) AS avg_price
	FROM track t
	JOIN album al 
		ON t.album_id = al.album_id
	GROUP BY al.title
	ORDER BY avg_price DESC;

-- Which playlists contain the most popular or expensive tracks?
-- Playlists with most expensive tracks
SELECT 
	p.name AS playlist_name, 
	COUNT(pt.track_id) AS track_count, 
	SUM(t.unit_price) AS total_price
FROM playlist p
JOIN playlist_track pt 
	ON p.playlist_id = pt.playlist_id
JOIN track t 
	ON pt.track_id = t.track_id
GROUP BY p.name
ORDER BY total_price DESC
LIMIT 10;

----------------------------------------------------------------------
-- 2. Customer and Invoices Analysis:
---------------------------------------------
-- What is the distribution of sales by customer location (country, city)?

SELECT 
	i.billing_country AS country, 
	i.billing_city AS city, 
	SUM(i.total) AS total_sales
FROM invoice i
GROUP BY i.billing_country, i.billing_city
ORDER BY total_sales DESC;


-- Which customers have the highest total spending?

SELECT 
	c.first_name, 
	c.last_name, 
	SUM(i.total) AS total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;

-- What is the average invoice amount?

SELECT AVG(total) AS average_invoice_amount
FROM invoice;

-- How does the number of items purchased impact total invoice value?

SELECT 
	i.invoice_id, 
	SUM(il.quantity) AS total_items, 
	i.total AS total_value
FROM invoice i
JOIN invoice_line il ON i.invoice_id = il.invoice_id
GROUP BY i.invoice_id
ORDER BY total_value DESC;


----------------------------------------------------------------------
-- 3. Artist and Album Insights:
---------------------------------------------

-- Which artists have the most tracks sold?

SELECT 
	a.name AS artist_name, 
	COUNT(il.track_id) AS tracks_sold
FROM artist a
JOIN album al ON a.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY a.artist_id
ORDER BY tracks_sold DESC
LIMIT 10;

-- What is the relationship between album sales and track popularity?

SELECT 
	al.title AS album,
	COUNT(il.track_id) AS track_count, 
	SUM(il.quantity * il.unit_price) AS album_sales
FROM album al
JOIN track t ON al.album_id = t.album_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY al.album_id
ORDER BY album_sales DESC;


-- How does the number of albums released by an artist correlate with total sales?

SELECT 
	a.name AS artist_name, 
	COUNT(al.album_id) AS albums_released, 
	SUM(il.unit_price * il.quantity) AS total_sales
FROM artist a
JOIN album al ON a.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY a.artist_id
ORDER BY total_sales DESC;



----------------------------------------------------------------------
-- 4. Playlist Insights:
---------------------------------------------

-- Which playlists are most popular based on the number of tracks?

SELECT 
	p.name AS playlist_name, 
	COUNT(pt.track_id) AS track_count
FROM playlist p
JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
GROUP BY p.playlist_id
ORDER BY track_count DESC
LIMIT 10;

-- What is the average length of playlists in terms of total track duration?

SELECT 
	DISTINCT p.name AS playlist_name, 
	AVG(t.milliseconds) AS average_duration
FROM playlist p
JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
JOIN track t ON pt.track_id = t.track_id
GROUP BY p.playlist_id
ORDER BY average_duration DESC;

----------------------------------------------------------------------
-- 5. Temporal Sales Trends:
---------------------------------------------

-- What are the monthly/quarterly trends in invoice generation (sales) over time?

---- Monthly trends
SELECT 
	EXTRACT(YEAR FROM i.invoice_date) AS year, 
	EXTRACT(MONTH FROM i.invoice_date) AS month, 
	SUM(i.total) AS total_sales
FROM invoice i
GROUP BY year, month
ORDER BY year, month;

---- Quarterly trends
SELECT EXTRACT(YEAR FROM i.invoice_date) AS year, EXTRACT(QUARTER FROM i.invoice_date) AS quarter, SUM(i.total) AS total_sales
FROM invoice i
GROUP BY year, quarter
ORDER BY year, quarter;

-- Are there any seasonal patterns in customer purchases or track popularity?

SELECT 
	EXTRACT(MONTH FROM i.invoice_date) AS month,
	SUM(i.total) AS total_sales
FROM invoice i
GROUP BY month
ORDER BY total_sales DESC;


----------------------------------------------------------------------
-- 6. Genre Popularity:
---------------------------------------------

-- Which genres contribute the most to overall sales?

SELECT 
	g.name AS genre, 
	SUM(il.unit_price * il.quantity) AS total_sales
FROM track t
JOIN genre g ON t.genre_id = g.genre_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY g.name
ORDER BY total_sales DESC;


-- What is the average track price per genre, and how does it compare across genres?

SELECT 
	g.name AS genre, 
	AVG(t.unit_price) AS avg_price
FROM track t
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY g.name
ORDER BY avg_price DESC;

-- Which genre has the longest tracks (by duration) or the most number of tracks?

---- Longest tracks by duration
SELECT 
	g.name AS genre, 
	AVG(t.milliseconds) AS avg_duration
FROM track t
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY g.name
ORDER BY avg_duration DESC;

---- Genre with the most number of tracks
SELECT 
	g.name AS genre, 
	COUNT(t.track_id) AS track_count
FROM track t
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY g.name
ORDER BY track_count DESC;


----------------------------------------------------------------------------------------------------------


