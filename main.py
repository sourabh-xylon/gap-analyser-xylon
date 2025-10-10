from gap_analyser_src.gap_finder import router as gap_finder
from fastapi import FastAPI

app = FastAPI()

app.include_router(gap_finder)

@app.get("/", tags=["home"])
def root():
    return {"message": "Gap Analyser API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
