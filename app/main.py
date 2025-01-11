from contextlib import asynccontextmanager
from anyio import to_thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Link Start!!!")

    limiter = to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1000

    yield
    print("Shutting down Server...")

app = FastAPI(
    title="Cloude",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    contact={
        "name": "Akashi",
        "url": "https://akashi.7o7.cx",
        "email": "abdulkid151@gmail.com"
    }
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/health')
async def hello():
    return {"status": "Ok!"}
