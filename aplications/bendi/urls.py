from django.urls import path
from aplications.bendi import views
app_name = "la_sucia_rata_de_la_bendi"

urlpatterns = [
    path("bendi_sucia/",views.bendi_view.as_view(),name='bendi_hdp'),
]