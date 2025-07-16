# Daytripper

Daytripper API plans optimised day trips by chaining together thousands of points of location data into flexible routes.

## Features

- FastAPI REST API
- PostgreSQL database integration
- Web scraping functionality

## Prerequisites

- Python 3.8+
- PostgreSQL
- Git

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SonnyRowland/daytripper
   cd daytripper
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Set up PostgreSQL database**

   ```bash
   # Create your database
   createdb daytripper_db
   # Run migrations if you have any
   ```

6. **Populate your database with data**
   ```bash
   # Navigate to scrapers folder
   cd app/scripts/scrapers
   # Run script to scrape web data
   python3 name_of_script_of_your_choice.py
   ```

## Usage

**Start the development server:**

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

**API Documentation:**

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

Copy `.env.example` to `.env` and configure:

```
DATABASE_URL=postgresql://username:password@localhost:5432/daytripper_db
DEBUG=True
# Add other variables as needed
```

## Project Structure

```
├── app/
│   ├── main.py          # FastAPI application
│   ├── config.py        # Configuration settings
│   ├── models/          # Database models
│   ├── routers/         # API routes
│   ├── scrapers/        # Web scraping modules
|   └── services/        # Business logic and operations
├── tests/               # Test files
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## API Endpoints

- `GET /` - Health check
- `GET /places/{id}` - Get place by id
- `GET /places/{postcode}` - Get places within postcode
- `GET /places/name/{name}` Get places that have the string given in the name

## License

MIT

## Contact

Sonny Rowland - sonnyrowland@gmail.com

Project Link: https://github.com/SonnyRowland/daytripper
