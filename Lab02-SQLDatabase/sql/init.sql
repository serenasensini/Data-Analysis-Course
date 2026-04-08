CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department VARCHAR(50) NOT NULL
);

INSERT INTO employees (name, age, salary, department) VALUES
('Alice', 25, 42000.00, 'HR'),
('Bob', 31, 56000.00, 'Sales'),
('Carla', 28, 48000.00, 'Marketing'),
('Diego', 45, 78000.00, 'Finance'),
('Eva', 32, 62000.00, 'IT'),
('Frank', 29, 50000.00, 'Sales'),
('Grace', 35, 65000.00, 'Marketing'),
('Henry', 38, 70000.00, 'Finance'),
('Isabella', 26, 55000.00, 'IT');

