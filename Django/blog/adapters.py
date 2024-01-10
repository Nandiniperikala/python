from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class KeycloakSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_login_redirect_url(self, request):
        # Replace 'your_keycloak_login_url' with the actual URL provided by Keycloak for login
        keycloak_login_url = 'http://localhost:8080/'
        return keycloak_login_url