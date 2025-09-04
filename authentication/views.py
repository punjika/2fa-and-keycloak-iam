
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

@login_required
def home(request):
	username = getattr(request.user, 'username', None)
	email = getattr(request.user, 'email', None)
	display_name = email if email else username if username else str(request.user)
	return HttpResponse(f'''
		<h1>Welcome to the Defense Login System!</h1>
		<p>You are logged in as: {display_name}</p>
		<a href="/auth/logout/">Logout</a>
	''')

def logout_view(request):
	django_logout(request)
	request.session.flush()
	keycloak_logout_url = (
		"http://localhost:8080/realms/defense-org/protocol/openid-connect/logout"
		"?redirect_uri=http://127.0.0.1:8000/oidc/authenticate/"
	)
	return redirect(keycloak_logout_url)

