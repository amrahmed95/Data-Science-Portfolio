# Music Store Data Analysis Project

This project analyzes a dataset from a fictional music store to uncover key business insights related to tracks, sales, customer behavior, Genres and Playlist, and more. The dataset includes information about tracks, albums, artists, customers, invoices, employees, and playlists.

## Table of Contents
- [Dataset Description](#dataset-description)
- [Project Overview](#project-overview)
- [Data Analysis Questions](#data-analysis-questions)
- [SQL Queries](#sql-queries)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Dataset Description

The dataset contains the following tables:

1. **Album**: Contains details about albums and their respective artists.
   - `album_id`, `title`, `artist_id`

2. **Artist**: Contains information about music artists.
   - `artist_id`, `name`

3. **Customer**: Contains customer information including location, contact details, and support representative assignment.
   - `customer_id`, `first_name`, `last_name`, `email`, `support_rep_id`, `city`, `country`

4. **Employee**: Contains employee information, including support representatives.
   - `employee_id`, `first_name`, `last_name`, `title`, `hire_date`

5. **Genre**: Contains music genre names.
   - `genre_id`, `name`

6. **Invoice**: Contains invoice data, including customer purchases and total amount.
   - `invoice_id`, `customer_id`, `invoice_date`, `total`, `billing_country`, `billing_city`

7. **Invoice Line**: Contains individual items from each invoice.
   - `invoice_line_id`, `invoice_id`, `track_id`, `unit_price`, `quantity`

8. **Track**: Contains details about each track in the music store, including price, genre, and duration.
   - `track_id`, `name`, `album_id`, `genre_id`, `milliseconds`, `unit_price`

9. **Playlist**: Contains playlists curated by customers or the store.
   - `playlist_id`, `name`

10. **Playlist Track**: Tracks associated with each playlist.
    - `playlist_id`, `track_id`

## Project Overview

This project focuses on answering key business questions using SQL queries. By analyzing sales, customer behavior, and playlist data, we aim to provide insights that could be used for business decisions such as marketing strategies, employee performance reviews, and sales optimization.

## Data Analysis Questions

The project addresses the following questions:

### Track and Sales Analysis
- Which tracks generate the highest revenue?
- How do sales vary by genre or media type?
- What is the average price per track, and how does it differ across genres or albums?
- Which playlists contain the most popular or expensive tracks?

### Customer and Invoices Analysis
- What is the distribution of sales by customer location (country, city)?
- Which customers have the highest total spending?
- What is the average invoice amount?
- How does the number of items purchased impact total invoice value?

### Artist and Album Insights
- Which artists have the most tracks sold?
- What is the relationship between album sales and track popularity?
- How does the number of albums released by an artist correlate with total sales?

### Playlist Insights
- Which playlists are most popular based on the number of tracks?
- What is the average length of playlists in terms of total track duration?

### Temporal Sales Trends
- What are the monthly/quarterly trends in invoice generation over time?
- Are there any seasonal patterns in customer purchases?

### Genre Popularity
- Which genres contribute the most to overall sales?
- What is the average track price per genre?
- Which genre has the longest tracks?

## SQL Queries

This project includes SQL queries to answer the above questions. Some key queries include:
- **Senior-most employee**: `Find the senior-most employee based on job title.`
- **Top customers by spending**: `Who is the best customer based on total spending?`
- **Sales by country and city**: `Identify the city with the highest total sales.`
- **Track revenue**: `Identify the tracks generating the highest revenue.`
- **Rock music fans**: `Find all customers who listen to rock music and invite them to a special event.`
- **Playlist length analysis**: `Calculate the average length of playlists by track duration.`


### Featured SQL Query:

One of the standout queries in this project is designed to uncover the customers' favorite genres and their total spending. This query highlights the SQL proficiency necessary to analyze consumer behavior and provide actionable business insights:

```sql
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    g.name AS favorite_genre,
    SUM(i.total) AS total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON il.track_id = t.track_id
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY c.customer_id, g.genre_id
ORDER BY total_spent DESC
LIMIT 10;
```

- **Purpose**: This query reveals the top 10 customers, their favorite genres, and how much they have spent, demonstrating your ability to extract valuable customer insights, crucial for personalized marketing and boosting sales.
  
You can find the full list of queries in the project files.

## Installation

To run this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/amrahmed95/Data-Science-Portfolio.git
    cd '.\Data Analysis\Music Store Analysis\'
    ```
   The project will be listed under the following repo:  
   `Data Science Portfolio > Data Analysis > Music Store Analysis`

2. **Install PostgreSQL** (if not already installed):
    Follow the [official PostgreSQL installation guide](https://www.postgresql.org/download/).

3. **Set up the database**:
   The SQL database is provided and called "Music_Store_database.sql". You can restore it inside any administrative and development platform for PostgreSQL.

4. **Run the SQL Queries**:
   You can run the provided SQL queries directly in your PostgreSQL database using a query editor or via command line.

## Usage

1. Import the dataset into a PostgreSQL database using the scripts provided.
2. Run the SQL queries to answer the business questions posed in the project.
3. Analyze the results to generate insights related to sales, customer behavior, and genres.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
