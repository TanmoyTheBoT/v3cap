from fastapi import FastAPI, HTTPException
import uvicorn

from .captcha import get_recaptcha_token
from .version import __version__

app = FastAPI(
    title="v3cap",
    version=__version__,
    description="Solve reCAPTCHA v3 challenges automatically",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/", tags=["Root"])
def root():
    return {
        "service": "v3cap",
        "status": "ok",
        "version": __version__,
    }

@app.post("/solve_recaptcha/", tags=["reCAPTCHA v3"])
async def solve_recaptcha(site_key: str, page_url: str, action: str):
    """
    API endpoint to solve a reCAPTCHA v3 challenge.
    
    Args:
        site_key: The reCAPTCHA site key
        page_url: The URL of the page containing the reCAPTCHA
        action: The action to perform on the reCAPTCHA
        
    Returns:
        JSON with the reCAPTCHA token
    """
    try:
        token = get_recaptcha_token(site_key, page_url, action)
        return {"gRecaptchaResponse": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def start_server(host="0.0.0.0", port=8000):
    """
    Start the FastAPI server.
    
    Args:
        host: Host to bind the server to
        port: Port to listen on
    """
    uvicorn.run(app, host=host, port=port) 