from django.shortcuts import render, HttpResponse
from UI.handler import UserHandler
from django.views import View

# Create your views here.
class UpdateAPI(View):
    def get(self, request):
        return HttpResponse('update api')
    def post(self, request):
        data = request.POST
        user_id = data.get('user_id')
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        UserHandler.update(id=user_id, name=name, username=username, email=email)
        user = UserHandler.get_user_by_id(user_id=user_id)
        return HttpResponse(user, content_type="application/json")
