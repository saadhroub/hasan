from django.urls import path
from . import views

urlpatterns = [
    path('shows/new/', views.new),
    path('shows/', views.shows),
    path('shows/create', views.create),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/destroy', views.destroy),
    path('', views.index),
    path('logreg', views.logreg),
    path('success', views.success),
    path('logout', views.logout),

]