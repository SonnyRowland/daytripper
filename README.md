# Daytripper

Daytripper API plans optimised day trips by chaining together thousands of points of location data into flexible routes. **Note:** this project contains images and opening times that are NOT true to the locations, and are simply included for demo purposes.

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

2. **Start the app!**

   ```bash
   pnpm install
   pnpm run dev
   ```

Docker will take care of the rest and the API will be available at `http://localhost:8000`

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

The web app will be available at `http://localhost:5173`

## Development

**Linting**

```bash
black app/
ruff check app/
ruff check app/ --fix

```

## Environment Variables

Copy `.env.example` to `.env` and configure:

```

DATABASE_URL=postgresql://username:password@localhost:5432/daytripper_db
DEBUG=True

```

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

Project Link: https://github.com/SonnyRowland/daytripper
