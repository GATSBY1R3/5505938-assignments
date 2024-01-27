CREATE TABLE IF NOT EXISTS movie_night (
    id SERIAL PRIMARY KEY,
    movie_title VARCHAR(255) NOT NULL,
    show_date DATE NOT NULL,
    genre VARCHAR(100),
    rating DECIMAL(2, 1)
);

INSERT INTO movie_night (movie_title, show_date, genre, rating)
VALUES
('Inception', '2024-02-05', 'Sci-Fi', 8.8),
('The Shawshank Redemption', '2024-02-12', 'Drama', 9.3),
('The Godfather', '2024-02-19', 'Crime', 9.2),
('Pulp Fiction', '2024-02-26', 'Thriller', 8.9);

SELECT movie_title, show_date, genre, rating
FROM movie_night
WHERE show_date >= CURRENT_DATE
ORDER BY show_date ASC
LIMIT 1;
