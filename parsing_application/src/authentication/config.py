import sys
sys.path.append("parsing_application/env_config.py")

from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from env_config import AUTH_SECRET

cookie_transport = CookieTransport(cookie_max_age=3600,
                                   cookie_name="parsing_app")

SECRET = AUTH_SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)