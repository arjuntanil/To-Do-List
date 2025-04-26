from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),  # Landing and home page (index.html)
    path('login/', views.login_view, name='login'),  # Login page with registration form
    path('register/', views.register_view, name='register'),  # Handle registration logic from login page
    path('logout/', views.logout_view, name='logout'),  # Logout functionality
    path('profile/', views.profile, name='profile'), 
    path('test/', views.test, name='test'),  
    path('create-task/', views.create_task, name='create_task'),      # URL for creating and viewing tasks
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('completed-tasks/', views.completed_tasks, name='completed_tasks'),
    path('todo-tasks/', views.todo_tasks, name='todo_tasks'),
    path('update-task-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
     path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('feedback/', views.feedback, name='feedback'),
    path('admin/feedback/', views.admin_feedback, name='admin_feedback'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    



