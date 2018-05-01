from django.shortcuts import render
from django.views import View
from UI.handler import UserHandler
# Create your views here.
class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        UserHandler.create_from_api()
        users = UserHandler.get_all_user()
        return render(request, self.template_name, locals())