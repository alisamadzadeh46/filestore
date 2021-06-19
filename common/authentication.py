from rest_framework.authentication import BaseAuthentication
import jwt, datetime
from filestore import settings


class JWTAuthentication:

    @staticmethod
    def generate_jwt(id, scope):
        payload = {
            'user_id': id,
            'scope': scope,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
