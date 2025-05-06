from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_recaptcha_token(site_key: str, page_url: str):
    """
    Solve a reCAPTCHA v3 challenge and return the token.
    
    Args:
        site_key: The reCAPTCHA site key
        page_url: The URL of the page containing the reCAPTCHA
        
    Returns:
        The reCAPTCHA token
    """
    chrome_options = Options()
    # Uncomment this to run in headless mode
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

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
            grecaptcha.execute(arguments[0], { action: 'auth_login' }).then(function(token) {
                callback(token);
            }).catch(function(error) {
                callback("ERROR: " + error.message);
            });
        """, site_key)

        if token.startswith("ERROR:"):
            raise Exception(token)

        return token

    except Exception as e:
        raise Exception(f"reCAPTCHA error: {str(e)}")
    finally:
        driver.quit() 