"""
URL configuration for SmoothStock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from contacts import views
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('to_do/', views.tasks, name='tasks'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),

    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    path('contacts/', views.contacts, name='contacts'),
    path('contact/create/', views.create_contact, name='create_contact'),
    #path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/list/', views.inventory_list, name='inventory_list'),
    path('inventory/product/<int:pk>', views.per_product_view, name='per_product'),
    path('inventory/add/', views.add_product, name='inventory_add'),
    path('inventory/delete/<int:pk>', views.delete_inventory, name='delete_inventory'),
    path('inventory/update/<int:pk>', views.update_inventory, name='update_inventory'),
]

handler404 = "tasks.views.handle_not_found"
