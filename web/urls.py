from django.urls import path
from web.views import index, details, about, department, details_dep

urlpatterns = [
    path('',index, name='home' ),
    path('about/',about, name='about' ),
    path('department/',department, name='department' ),
    path('details_dep/<int:id>',details_dep, name='details_dep' ),
    path('details/<int:id>',details, name='details' ),
]