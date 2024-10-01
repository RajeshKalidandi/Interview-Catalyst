# Interview Catalyst

An automated job application assistant with FastAPI backend and React frontend.

## Project Structure
Interview-Catalyst/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
│ ├── job_scraper.py
│ ├── celery_app.py
│ ├── models/
│ └── routers/
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── package-lock.json
├── venv/
├── .env
├── .gitignore
├── requirements.txt
├── run_celery.bat
├── run_celery_beat.bat
└── celery_config.py

## Backend (FastAPI)

- Set up FastAPI application with CORS middleware
- Implemented Supabase integration for database operations
- Created job scraping functionality using Playwright
- Set up Celery for task scheduling and background job processing
- Implemented endpoints for triggering job scraping and retrieving job listings

## Frontend (React)

- Set up basic React application using create-react-app
- Installed Material-UI for styling

## Task Scheduling

- Configured Celery with Redis for periodic job scraping tasks
- Created batch files for running Celery worker and beat scheduler on Windows

## Current Functionality

1. Job scraping from LinkedIn
2. Storing job listings in Supabase database
3. Retrieving job listings via API endpoint
4. Periodic job scraping using Celery beat scheduler

## Next Steps

1. Implement user authentication
2. Develop frontend UI for displaying job listings
3. Add functionality for users to apply to jobs
4. Implement more job sources for scraping
5. Add filtering and search capabilities for job listings

## Setup and Running

(Add instructions for setting up and running the project, including environment variables, database setup, and running the frontend and backend)

## Contributing

(Add guidelines for contributing to the project)

## License

(Add license information if applicable)
