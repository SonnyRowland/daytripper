# Daytripper

Daytripper API plans optimised day trips by chaining together thousands of points of location data into flexible routes.

## Features

- FastAPI REST API
- PostgreSQL database integration
- Web scraping functionality
- Docker containerisation for easy setup

## Quick start with docker

1. **Clone the repository**

   ```bash
   git clone https://github.com/SonnyRowland/daytripper
   cd daytripper
   ```

2. **Start the API**

   ```bash
   docker-compose up --build
   ```

3. **Run vite**
   ```bash
   cd client/daytripper
   pnpm run dev
   ```

The API will be available at `http://localhost:8000`

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

The app will be available at `http://localhost:5173`

## Development

**Linting**

```bash
black app/
ruff check app/
ruff check app/ --fix

## Environment Variables

Copy `.env.example` to `.env` and configure:

```

DATABASE_URL=postgresql://username:password@localhost:5432/daytripper_db
DEBUG=True

## Project Structure

```

├── app/
│ ├── main.py # FastAPI application
│ ├── config.py # Configuration settings
│ ├── models/ # Database models
│ ├── routers/ # API routes
│ ├── scrapers/ # Web scraping modules
| └── services/ # Business logic and operations
├── tests/ # Test files
├── requirements.txt # Dependencies
└── README.md # This file

```

## API Endpoints

- `GET /` - Health check
- `GET /places/{id}` - Get place by id
- `GET /places/{postcode}` - Get places within postcode
- `GET /places/name/{name}` Get places that have the string given in the name
- `GET /places/walk/{id}/{length}` Get walk starting at id of given length

## License

MIT

## Contact

Sonny Rowland - sonnyrowland@gmail.com

Project Link: https://github.com/SonnyRowland/daytripper

```

```
