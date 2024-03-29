CREATE TABLE company (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  business TEXT,
  mvv TEXT,
  required_skill TEXT,
  location TEXT,
  benefit TEXT,
  applying_motivation TEXT
);

CREATE TABLE company_connection (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  company_id INT NOT NULL,
  connection_date DATE NOT NULL,
  way TEXT,
  employee TEXT,
  content TEXT NOT NULL,
  route TEXT,
  FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE CASCADE
);
