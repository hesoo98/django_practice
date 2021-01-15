from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin  # 뷰 처리 진입 단계에서 적절한 권한을 갖췄는지 판별할 때 쓰는 믹스인 클래스.


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):  # 로그인한 사용자가 콘텐츠의 소유자인지를 판별합니다.
    raise_exception = True          # 소유자가 아닐시 이 속성이 True 면 403 익셉션 처리, False 면 로그인 페이지 리다이렉트.
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:                       # 현재 사용자(request.user)와 객체의 소유자(obj.owner)
            return self.handle_no_permission()              # 가 다르면 403익셉션 처리
        return super().dispatch(request, *args, **kwargs)   # 같으면 정상 처리.
