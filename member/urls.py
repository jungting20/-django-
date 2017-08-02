from django.conf.urls import url

from member.views import joinmember, login, joinmemberajax

from django.contrib.auth import views

urlpatterns = [
    url(r'^join/$',joinmember,name='joinmember'),
    url(r'^login/$',login,name='login',),
    url(r'^logout/$',views.logout,name='logout',kwargs={
        'next_page':'login'
    }),
    url(r'^ajaxjoinmember/$',joinmemberajax,name='ajaxjoin')
]

