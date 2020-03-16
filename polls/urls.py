from django.urls import path, include, re_path

# L1 https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail?rq=1
from django.views.static import serve 
from django.conf import settings

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.QuestionView.as_view(), name='question'),

    # ex: /polls/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact_email, name='contact'),
    path('contact_email_sent/', views.contact_email_sent, name='contact_email_sent'),

    path('email/', views.email, name='email'),

    path('barcode_req/', views.barcode_req, name='barcode_req'),
    path('barcode_disp/', views.barcode_disp, name='barcode_disp'),

    path('upload_file/', views.upload_file, name='upload_file'),
    path('upload_success/', views.upload_success, name='upload_success'),

    path('view_file_tree/', views.view_file_tree, name='view_file_tree'),


    re_path(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT }), 
    re_path(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }), 
]
