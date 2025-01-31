import uvicorn

from fastapi import FastAPI

from routers import legislation


app = FastAPI()
app.include_router(legislation.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5002,
                reload=True, log_level='debug')
