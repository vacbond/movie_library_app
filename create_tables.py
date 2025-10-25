import db

cur, conn = db.get_connection()

# Create the first table - movies table

cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id SERIAL PRIMARY KEY,
        tmdb_movie_id INTEGER UNIQUE NOT NULL,
        title VARCHAR(255) NOT NULL,
        release_date DATE,
        runtime INTEGER,
        rating DECIMAL(3,1),
        vote_count INTEGER,
        popularity DECIMAL(6,2),
        overview TEXT,
        favorite BOOLEAN DEFAULT FALSE NOT NULL,
        watchlist BOOLEAN DEFAULT FALSE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
    """)

conn.commit()

# Create the second table - series table

cur.execute("""
    CREATE TABLE IF NOT EXISTS series (
        id SERIAL PRIMARY KEY,
        tmdb_series_id INTEGER UNIQUE NOT NULL,
        title VARCHAR(255) NOT NULL,
        release_date DATE,
        runtime INTEGER,
        rating DECIMAL(3,1),
        vote_count INTEGER,
        popularity DECIMAL(6,2),
        overview TEXT,
        favorite BOOLEAN DEFAULT FALSE NOT NULL,
        watchlist BOOLEAN DEFAULT FALSE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
    """)

conn.commit()

# Create the third table - genres table

cur.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id SERIAL PRIMARY KEY,
        tmdb_genre_id INTEGER UNIQUE NOT NULL,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        type VARCHAR(10) NOT NULL,  -- movie / series
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
    """)

conn.commit()

# Create the fourth table - movie_genres

cur.execute("""
    CREATE TABLE IF NOT EXISTS movie_genres (
        movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
        genre_id INTEGER REFERENCES genres(id) ON DELETE CASCADE,
        PRIMARY KEY (movie_id, genre_id)
    );
    """)

conn.commit()

# Create the fifth table - series_genres

cur.execute("""
    CREATE TABLE IF NOT EXISTS series_genres (
        series_id INTEGER REFERENCES series(id) ON DELETE CASCADE,
        genre_id INTEGER REFERENCES genres(id) ON DELETE CASCADE,
        PRIMARY KEY (series_id, genre_id)
    );
    """)

conn.commit()

print("Tables created/checked successfully.")
