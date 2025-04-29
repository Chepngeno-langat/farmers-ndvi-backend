import os
import uvicorn
from main import app  # import your FastAPI app from your main.py (adjust if needed)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Railway's port or fallback to 8000 locally
    uvicorn.run(app, host="0.0.0.0", port=port)
