CREATE TABLE IF NOT EXISTS
    driver_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    vehicle_type VARCHAR(50) NOT NULL,
    vehicle_number VARCHAR(20) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5),
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS
    passenger_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    last_ride TIMESTAMP,
    last_ride_vechicle_number VARCHAR(20) NOT NULL
    -- Assuming last_ride_vehicle_number is a reference to vehicle_number in driver_data
);

    CREATE  TABLE IF NOT EXISTS
    ride_data (
    id SERIAL PRIMARY KEY,
    driver_id INT NOT NULL,
    passenger_id INT NOT NULL,
    start_location VARCHAR(255) NOT NULL,
    end_location VARCHAR(255) NOT NULL,
    fare DECIMAL(10, 2) NOT NULL,
    ride_status VARCHAR(20) NOT NULL DEFAULT 'ongoing',
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES driver_data(id) ON DELETE CASCADE,
    FOREIGN KEY (passenger_id) REFERENCES passenger_data(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS
    feedback_data (
    id SERIAL PRIMARY KEY,
    ride_id INT NOT NULL,
    passenger_id INT NOT NULL,
    driver_id INT NOT NULL,
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ride_id) REFERENCES ride_data(id) ON DELETE CASCADE,
    FOREIGN KEY (passenger_id) REFERENCES passenger_data(id) ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES driver_data(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS
    payment_data (
    id SERIAL PRIMARY KEY,
    ride_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(20) NOT NULL DEFAULT 'pending',
    payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ride_id) REFERENCES ride_data(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS
    emergency_contact_data (
    id SERIAL PRIMARY KEY,
    passenger_id INT NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    contact_phone_number VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (passenger_id) REFERENCES passenger_data(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS
    driver_availability (
    id SERIAL PRIMARY KEY,
    driver_id INT NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES driver_data(id) ON DELETE CASCADE
);          