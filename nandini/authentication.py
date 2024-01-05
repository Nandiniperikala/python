# from rest_framework.authentication import BaseAuthentication
# from keycloak import KeycloakOpenID
# from django.shortcuts import redirect


# class KeycloakAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         # Your authentication logic here using python-keycloak
#         # Example:
#         token = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[-1]
#         keycloak_openid = KeycloakOpenID(server_url='http://localhost:8080/',
#                                client_id='DjangoClient',
#                                realm_name='djangorealm',
#                                client_secret_key="RK9u4u0xa1k3wRvKOTpuPUoGTtEYxRhM")
        
        
#         introspection_result = keycloak_openid.introspect(token)
#         #user_info = keycloak_openid.decode_token(token)
#         if introspection_result.get('active'):
        
#         # Create or retrieve Django user based on user_info
#         # Example:
#             user, created = User.objects.get_or_create(username=introspection_result['username'])

#             if created:
#                 user.is_active = True
#                 user.save()
        
#             return user, None

#         return None

############################################################################################################

# from rest_framework.authentication import BaseAuthentication
# from keycloak import KeycloakOpenID
# from django.contrib.auth.models import User
# import logging


# logger = logging.getLogger(__name__)

# class KeycloakAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         # Your authentication logic here using python-keycloak
#         # Example:
#         token = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[-1]
#         keycloak_openid = KeycloakOpenID(server_url='http://localhost:8080/',
#                                client_id='DjangoClient',
#                                realm_name='djangorealm',
#                                client_secret_key="RK9u4u0xa1k3wRvKOTpuPUoGTtEYxRhM")

#         logger.debug(f"Received token: {token}")

#         introspection_result = keycloak_openid.introspect(token)
#         logger.debug(f"Introspection result: {introspection_result}")

#         if introspection_result.get('active'):
#             # Create or retrieve Django user based on introspection_result
#             # Example:
#             username = introspection_result.get('username')
#             if not username:
#                 logger.error("Username not found in introspection result.")
#                 return None

#             user, created = User.objects.get_or_create(username=username)

#             if created:
#                 user.is_active = True
#                 user.save()
#                 logger.info(f"User {username} created and activated.")
#             else:
#                 logger.info(f"User {username} retrieved.")

#             return user, None

#         logger.warning("Token is not active.")
#         return None



from rest_framework.authentication import BaseAuthentication
from keycloak import KeycloakOpenID
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import logging


logger = logging.getLogger(__name__)

class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Your authentication logic here using python-keycloak
        # Example:
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split('Bearer ')[1]

        keycloak_openid = KeycloakOpenID(
            server_url='http://localhost:8080/',
            client_id='DjangoClient',
            realm_name='djangorealm',
            client_secret_key="RK9u4u0xa1k3wRvKOTpuPUoGTtEYxRhM"
        )

        logger.debug(f"Received token: {token}")

        introspection_result = keycloak_openid.introspect(token)
        logger.debug(f"Introspection result: {introspection_result}")

        if introspection_result.get('active'):
            # Create or retrieve Django user based on introspection_result
            # Example:
            username = introspection_result.get('username')
            if not username:
                logger.error("Username not found in introspection result.")
                raise AuthenticationFailed("Username not found in introspection result.")

            user, created = User.objects.get_or_create(username=username)

            if created:
                user.is_active = True
                user.save()
                logger.info(f"User {username} created and activated.")
            else:
                logger.info(f"User {username} retrieved.")

            return user, None

        logger.warning("Token is not active.")
        raise AuthenticationFailed("Token is not active.")



