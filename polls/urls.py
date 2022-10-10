from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #mysite/urls에서 polls를 잡아내어 여기로 연결해주면
    #polls/ 뒤에 아무것도""없으니 view.index라는 view내뷰로 연결시켜줌
    #view내부에서는 httpresponse로 helloworld를 반환해준다

]