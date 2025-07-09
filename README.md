# SECURE_FEMALE_TAXI

**A secure and reliable taxi service for women.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Objective

SECURE_FEMALE_TAXI aims to provide a safe and secure transportation solution for women. Our platform offers enhanced security features to ensure peace of mind for both passengers and their families.

## How it Works

The platform provides a multi-faceted approach to security:

1.  **Driver Verification:** Before starting a trip, passengers can verify their driver's identity by Either one of these:
    *   Scanning the driver's face using their smartphone camera.
    *   Scanning a unique QR code assigned to each driver and vehicle.

    This verification process provides the passenger with crucial information about the driver, including:
    *   Total number of trips completed.
    *   Success rate of completed trips.
    *   Accident history.
    *   Number of reports filed against the driver.
    *   Vehicle and driver details.

2.  **Real-time Trip Monitoring:** During the trip, the passenger's smartphone will securely transmit sensor data to our servers for real-time analysis. This data includes:
    *   **Microphone:** Audio data is monitored for signs of distress or unusual activity.
    *   **GPS:** Real-time location tracking.
    *   **Camera:** The camera can be activated if a potential threat is detected.
    *   **Motion Sensors:** Data from the accelerometer and gyroscope can help detect sudden stops, erratic driving, or accidents.

3.  **AI-Powered Threat Detection:** All sensor data is encrypted and analyzed by our AI/ML models to detect potential threats and accidents in real-time. If the system detects a high-risk situation, it can automatically alert emergency services and designated contacts.

## Tech Stack

*   **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Database:** [PostgreSQL](https://www.postgresql.org/)
*   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
*   **Computer Vision:** [OpenCV](https://opencv.org/)
*   **Data Validation:** [Pydantic](https://pydantic-docs.helpmanual.io/)

## Getting Started

**Prerequisites:**

*   Python 3.11+
*   PostgreSQL

**Installation:**

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/SECURE_FEMALE_TAXI.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set up the database:
    *   Create a PostgreSQL database.
    *   Copy the `.env.example` file to `.env` and update the database credentials.
4.  Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Contributing

We welcome contributions to SECURE_FEMALE_TAXI! Please see our `CONTRIBUTING.md` file for more information on how to get involved.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.