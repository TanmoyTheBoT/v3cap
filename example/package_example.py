"""
Example: Using v3cap as a Python package to solve reCAPTCHA v3.
"""

from v3cap import get_recaptcha_token

def main():
    site_key = "6LcwvFgrAAAAAG5UjzyiOkNe-3ekjPHJv0FUzeVy"
    page_url = "https://demo-v3cap.vercel.app"
    action = "demo/v3cap"

    try:
        token = get_recaptcha_token(site_key, page_url, action)
        print("Token:", token)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
