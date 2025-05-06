from fastapi import FastAPI, HTTPException
import uvicorn
from .captcha import get_recaptcha_token

app = FastAPI()

@app.post("/solve_recaptcha/")
async def solve_recaptcha(site_key: str, page_url: str):
    """
    API endpoint to solve a reCAPTCHA v3 challenge.
    
    Args:
        site_key: The reCAPTCHA site key
        page_url: The URL of the page containing the reCAPTCHA
        
    Returns:
        JSON with the reCAPTCHA token
    """
    try:
        token = get_recaptcha_token(site_key, page_url)
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