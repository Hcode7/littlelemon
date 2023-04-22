from django.urls import path
from . import views
from .views import MenuItemView
from .views import MenuSingleItemView

urlpatterns = [
    path('menu/',views.menu, name='menu'),
    path('about/',views.about, name='about'),
    path('book/',views.book, name='book'),
    path('menu-item/<int:pk>/', views.display_menu_items, name="menu-item"),
    path('',views.home, name='home'),
    path('api-menu/',MenuItemView.as_view()),
    path('api-menu/<int:pk>',MenuSingleItemView.as_view()),



]
