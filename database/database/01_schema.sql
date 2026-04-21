CREATE DATABASE IF NOT EXISTS semis_ewaste;

USE semis_ewaste;

CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bin_id VARCHAR(10),
    fill_percent DECIMAL(5,1),
    temperature DECIMAL(5,1),
    risk_level VARCHAR(20),
    waste_type VARCHAR(50),
    green_score DECIMAL(5,1),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gamification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    citizen_id VARCHAR(20),
    points INT DEFAULT 0,
    badges VARCHAR(100),
    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
