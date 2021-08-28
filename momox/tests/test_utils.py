# from django.contrib.auth import get_user_model
#
# from momox.apps.token_auth.models import TokenAuth
#
# User = get_user_model()
#
#
# def get_token_authentication_headers(user):
#     token = TokenAuth.objects.get(user_id=user.id)
#     return {"Authorization": f"Bearer {token.token}"}
