from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()


@app.get('/')
def root():
    return PlainTextResponse('HELLO', status_code=200)


@app.post('/')
def process_data(message: str):
    return JSONResponse(content={'data': message}, status_code=200)
