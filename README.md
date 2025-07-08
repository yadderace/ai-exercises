# Connect4 AI Game

A Connect4 game implementation with AI opponent using FastAPI backend and React frontend.

## Project Structure

```
ai-exercises/
├── connect4-backend/      # FastAPI backend with AI implementation
│   ├── app/
│   │   ├── main.py      # Main FastAPI application
│   │   └── ai.py        # AI implementation
│   ├── requirements.txt
│   └── Dockerfile
├── connect4-frontend/    # React frontend
│   ├── src/
│   ├── package.json
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml    # Configuration for running both services together
```

## Backend (FastAPI)

### Purpose
The backend provides a REST API for the Connect4 game with:
- Game state management
- AI opponent implementation using Minimax algorithm
- API endpoints for game moves and state

### Setup
1. Create virtual environment:
```bash
cd connect4-backend
python -m venv venv-connect4-backend
source venv-connect4-backend/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Independently
```bash
cd connect4-backend
source venv-connect4-backend/bin/activate
python -m app.main
```

The backend will run on `http://localhost:8000`

## Frontend (React)

### Purpose
The frontend provides a modern web interface for playing Connect4 against the AI opponent.

### Setup
1. Install dependencies:
```bash
cd connect4-frontend
npm install
```

### Running Independently
```bash
cd connect4-frontend
npm run dev
```

The frontend will run on `http://localhost:5173`

## Running Together with Docker

### Prerequisites
- Docker and Docker Compose installed

### Build and Run
```bash
docker-compose up --build
```

This will:
1. Build both Docker images
2. Start both services
3. Set up networking between them

### Accessing the Application
- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:8000`

### Available API Endpoints
- `GET /reset` - Reset the game
- `GET /play?player_col=X` - Make a move in column X

## Project Features

### Backend Features
- FastAPI REST API
- Minimax AI implementation
- Game state persistence
- API documentation at `/docs`

### Frontend Features
- Modern React interface
- Real-time game visualization
- AI decision tree visualization
- Responsive design

## Development

### Backend Development
- API documentation available at `/docs`
- Hot reload enabled
- Python type hints
- CORS enabled for frontend integration

### Frontend Development
- Vite for fast development
- React + TypeScript
- Hot module replacement
- Tree visualization using react-d3-tree

## License

MIT License
