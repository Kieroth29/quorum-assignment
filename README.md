# Installation instructions

## Back-end

- Navigate to the "backend" folder and create a virtual environment (preferably using Python 3.11.3).
- Install the dependencies using `pip install -r requirements.txt`.
- Then, run the application with Uvicorn: `uvicorn main:app --port 5002`.
- The web server documentation will be available at http://localhost:5002/docs

## Front-end

- Install "pnpm" globally using `pnpm install -g`
- Navigate to the "frontend" folder.
- Install project dependencies using `pnpm install`
- Run the frontend: `pnpm dev`
- The interface will be available by default at http://localhost:3000, but the port may change depending on availability. This will be informed on the console.
