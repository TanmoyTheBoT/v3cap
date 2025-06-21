# Version information
from .version import __version__

# Core functionality
from .captcha import get_recaptcha_token
from .api import start_server

__all__ = [
    "get_recaptcha_token",
    "start_server",
    "__version__",
]

# Package metadata
__author__ = "TanmoyTheBoT"
__package_name__ = "v3cap"