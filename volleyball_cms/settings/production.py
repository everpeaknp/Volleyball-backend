from .base import *

DEBUG = False


def _split_csv_env(name, default=''):
    raw = os.environ.get(name, default)
    return [item.strip() for item in raw.split(',') if item.strip()]


ALLOWED_HOSTS = _split_csv_env(
    'ALLOWED_HOSTS',
    'nvchhamburg.de,www.nvchhamburg.de',
)

CSRF_TRUSTED_ORIGINS = _split_csv_env(
    'CSRF_TRUSTED_ORIGINS',
    'https://nvchhamburg.de,https://www.nvchhamburg.de',
)

# Trust HTTPS forwarded by reverse proxy (Nginx/Cloudflare).
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
