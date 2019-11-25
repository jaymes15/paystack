from django.urls import path
from . import views



app_name= 'paystack'
urlpatterns = [
    path('', views.banklist,name='banklist'),
    path('bankdetail/<int:bank_id>', views.bankdetail,name='bankdetail'),
]

'''
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
'''

