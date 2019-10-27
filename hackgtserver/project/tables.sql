CREATE TABLE Users(
    id INT AUTO_INCREMENT,
    username varchar(16) NOT NULL,
    password varchar(255) NOT NULL
    PRIMARY KEY ukey (username)
);
CREATE TABLE Images(
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    message TEXT,
    photo BLOB NOT NULL,
    processed TINYINT,
    PRIMARY KEY imagesKey (id, name),
    FOREIGN KEY imagesForeignKey (id) REFERENCES Users(id)
);