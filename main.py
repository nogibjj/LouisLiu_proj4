from fastapi import FastAPI
import uvicorn
from gcpconn import topFivePosts

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/topfive")
async def topfive():
    """Print the top five ranking stackoverflow posts"""

    result = topFivePosts()

    return {"result: ": result}


# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")