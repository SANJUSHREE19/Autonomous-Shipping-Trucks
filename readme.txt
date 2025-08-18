# Autonomous Trucks Management System

A web-based fleet management system for monitoring, tracking, and managing autonomous trucks. This application allows users to track truck locations, manage schedules, request services, and receive alerts in real-time.

## Features

- **Real-time Truck Tracking**: View truck locations on an interactive map
- **Fleet Management**: Add, update, and delete trucks from the fleet
- **Scheduling System**: Schedule routes and deliveries for trucks
- **Service Requests**: Request maintenance and other services for trucks
- **Alert System**: Receive real-time alerts about truck status and issues
- **User Authentication**: Secure login and registration system
- **User Profiles**: Manage user information and preferences
- **Simulation Tools**: Run simulations to test truck behavior in various scenarios
- **Reporting**: Generate reports on truck performance and fleet status

## Technology Stack

- **Backend**: Python with Flask web framework
- **Database**: MongoDB for data storage
- **Frontend**: HTML, CSS, JavaScript
- **Maps API**: Google Maps API for location tracking
- **Authentication**: Session-based authentication with password hashing

## Project Structure

```
AUTONOMOUS_TRUCKS/
├── __pycache__/
├── static/
│   └── styles.css
├── templates/
│   ├── add_truck.html
│   ├── alerts.html
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   ├── register.html
│   ├── reports.html
│   ├── request_service.html
│   ├── schedule.html
│   ├── simulation.html
│   ├── track_map.html
│   ├── track_trucks.html
│   └── update.html
├── app.py
├── db.py
├── models.py
└── readme.txt
```

## Setup Instructions

### Prerequisites

- Python 3.7
- MongoDB 4.0 or higher
- Google Maps API key
- Carla 0.9.14

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/autonomous-trucks.git
   cd autonomous-trucks
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install flask pymongo werkzeug
   ```

4. Configure MongoDB:
   - Ensure MongoDB is running on your system
   - The application is configured to connect to `mongodb://localhost:27017/`
   - Database name: `autonomous_trucks`

5. Set up Google Maps API:
   - Obtain a Google Maps API key from the Google Cloud Console
   - Add your API key to the Flask app configuration in `app.py`

6. Run the application:
   ```
   python app.py
   ```

7. Access the application at `http://localhost:5000`

## Usage

### User Management

- Register a new account at `/register`
- Log in to your account at `/login`
- View and edit your profile at `/profile`

### Truck Management

- View all trucks on the dashboard at `/`
- Add a new truck at `/add`
- Update truck status at `/update/<truck_id>`
- Delete a truck at `/delete/<truck_id>`

### Tracking

- View truck locations on a list at `/track_trucks`
- View truck locations on a map at `/track_map`

### Scheduling and Service

- Manage truck schedules at `/schedule`
- Request service for trucks at `/request_service`

### Analytics and Alerts

- View reports at `/reports`
- View and manage alerts at `/alerts`
- Run simulations at `/simulation`

## Security Features

- Password hashing using Werkzeug's security functions
- Session-based authentication
- Login required decorator for protected routes


## License

This project is licensed under the MIT License - see the LICENSE file for details.

