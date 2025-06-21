import time
from seleniumbase import Driver

def get_recaptcha_token(site_key: str, page_url: str, action: str):
    """
    Solve a reCAPTCHA v3 challenge and return the token.
    
    Args:
        site_key: The reCAPTCHA site key
        page_url: The URL of the page containing the reCAPTCHA
        action: The action to perform on the reCAPTCHA

    Returns:
        The reCAPTCHA token
    """
    driver = Driver(
        uc=True,
        headless=True,
        chromium_arg="--no-sandbox,--disable-dev-shm-usage,--disable-gpu,--window-size=1920,1080"
    )
    try:
        driver.get(page_url)
        time.sleep(3)  # Let the page and scripts load

        # Wait for grecaptcha to be available
        for i in range(10):
            has_grecaptcha = driver.execute_script("return typeof grecaptcha !== 'undefined' && typeof grecaptcha.execute === 'function';")
            if has_grecaptcha:
                break
            time.sleep(1)
        else:
            raise Exception("grecaptcha not loaded on the page")

        # Execute grecaptcha and wait for token
        token = driver.execute_async_script("""
            var callback = arguments[arguments.length - 1];
            grecaptcha.execute(arguments[0], { action: arguments[1] }).then(function(token) {
                callback(token);
            }).catch(function(error) {
                callback("ERROR: " + error.message);
            });
        """, site_key, action)

        if token.startswith("ERROR:"):
            raise Exception(token)

        return token

    except Exception as e:
        raise Exception(f"reCAPTCHA error: {str(e)}")
    finally:
        driver.quit() 