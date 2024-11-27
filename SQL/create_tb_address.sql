CREATE TABLE tb_address (
    id INTEGER NOT NULL AUTO_INCREMENT,
    city VARCHAR(120) NOT NULL,
    state VARCHAR(120) NOT NULL,
    lake_name VARCHAR(120),
    capybara_id INTEGER,
    PRIMARY KEY (id),
    UNIQUE (capybara_id),
    FOREIGN KEY(capybara_id) REFERENCES tb_capybara (id)
)