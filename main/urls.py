from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('calculator', views.calc),
    path('banking', views.bank, name='bankk'),
    path('create', views.create),
    path('<int:pk>', views.BanksDetailView.as_view(), name='banks-detail'),
    path('<int:pk>/update', views.BanksUpdateView.as_view(), name='banks-update'),
    path('<int:pk>/delete', views.BanksDeleteView.as_view(), name='banks-delete')

]
