from django.urls import path

from . import views

app_name = 'pens'

urlpatterns = [
    path('pen/add',views.edit_pen,name='add_pen'),
    path('pen/edit/<int:pen_id>',views.edit_pen,name='edit_pen'),
    path('pen/delete/<int:pen_id>',views.delete_pen,name='delete_pen'),
    path('pen/',views.index,name='index'),
    
]
