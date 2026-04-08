CREATE TABLE IF NOT EXISTS movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    imdb_rating DECIMAL(3, 1) NOT NULL,
    release_year INT NOT NULL,
    genre VARCHAR(80) NOT NULL,
    duration_minutes INT NOT NULL
);

