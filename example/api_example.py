"""
Example: Using v3cap API to solve reCAPTCHA v3.
"""

import requests

def solve_recaptcha(site_key: str, page_url: str, action: str) -> dict:
    api_url = "http://localhost:8000/solve_recaptcha/"
    response = requests.post(api_url, params={
        "site_key": site_key,
        "page_url": page_url,
        "action": action
    })
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Example values
    site_key = "6LcwvFgrAAAAAG5UjzyiOkNe-3ekjPHJv0FUzeVy"
    page_url = "https://demo-v3cap.vercel.app"
    action = "demo/v3cap"

    print("Requesting reCAPTCHA token...")
    try:
        result = solve_recaptcha(site_key, page_url, action)
        print("Token:", result["gRecaptchaResponse"])
    except Exception as e:
        print("Error:", e)
