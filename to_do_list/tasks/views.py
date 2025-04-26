from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm  # Ensure you have a TaskForm form for handling task creation and updates
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Feedback
from django.http import HttpResponseForbidden
import re



# Landing and home page view (index.html)
def index_view(request):
    return render(request, 'tasks/index.html')

# Login view (login.html)
# Login view (login.html)
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('index')  # Redirect to home/landing page (index.html) after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'tasks/login.html')  # Stay on the login page with error message

    return render(request, 'tasks/login.html')  # Default to the login page if not POST request

# Registration view (handle registration from login.html)
# Registration view (handle registration from login.html)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if len(username) < 4:  # Check username length
            messages.error(request, 'Username must be at least 4 characters long.')
        # Check if the username or email already exists
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            
        elif password != confirm_password:  # Check if passwords match
            messages.error(request, 'Passwords do not match.')
            
        else:
            # Password validation
            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
            elif not re.search(r'[A-Z]', password):
                messages.error(request, 'Password must contain at least one uppercase letter.')
            elif not re.search(r'[a-z]', password):
                messages.error(request, 'Password must contain at least one lowercase letter.')
            elif not re.search(r'[0-9]', password):
                messages.error(request, 'Password must contain at least one digit.')
            elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                messages.error(request, 'Password must contain at least one special character.')
            else:
                # Create the new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Redirect to login with success message
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
    
    # Render the registration form
    return render(request, 'tasks/login.html')

# Logout view
# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('index')  # Redirect to the landing page (index.html) after logout

@login_required
def profile(request):
    
    return render(request, 'tasks/profile.html')
    

def test(request):
    
    return render(request,'tasks/test.html')


# Create and display tasks
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()  # Save the new task to the database
            return redirect('create_task')  # Redirect to refresh the task list
    else:
        form = TaskForm()
    
    # Fetch only the tasks of the logged-in user
    tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
    return render(request, 'tasks/create_task.html', {'form': form, 'tasks': tasks})


def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        # Redirect if the task does not exist
        return redirect('create_task')

    # Ensure the task belongs to the logged-in user
    if task.user != request.user:
        return redirect('create_task')

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()

        return redirect('todo_tasks')  # Redirect to 'To-Do' page

    return render(request, 'tasks/edit_task.html', {'task': task})
    # Render the task details if method is GET
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure the task belongs to the logged-in user
    task.delete()
    return redirect('create_task')

@login_required
# View for Completed Tasks
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, status='completed')  # Get completed tasks for the logged-in user
    return render(request, 'tasks/completed_task.html', {'tasks': tasks})
    

# View for To-Do Tasks
@login_required
def todo_tasks(request):
    tasks = Task.objects.filter(user=request.user, status='todo')  # Get to-do tasks for the logged-in user
    return render(request, 'tasks/todo.html', {'tasks': tasks})
    

# View to update task status to 'completed' and move to completed tasks page
def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Ensure the task belongs to the logged-in user
    task.status = 'completed'
    task.save()
    return redirect('completed_tasks')  # Redirect to the completed tasks page
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
import string

# View for Forgot Password
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = str(random.randint(100000, 999999))  # Generate a 6-digit OTP

            # Store OTP in session
            request.session['reset_otp'] = otp
            request.session['reset_email'] = email  # Store email for later use

            # Send the OTP to the user's email
            send_mail(
                'Password Reset OTP',
                f'Your OTP for resetting your password is: {otp}',
                'noreply@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, "An OTP has been sent to your email.")
            return redirect('verify_otp')  # Redirect to OTP verification page
        except User.DoesNotExist:
            messages.error(request, "No user found with this email.")
    
    return render(request, 'tasks/forgot_password.html')

# View for OTP Verification
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')  # Get the OTP entered by the user
        session_otp = request.session.get('reset_otp')  # Get the OTP stored in the session
        
        # Debugging: Print both OTPs for comparison
        print(f"Entered OTP: {entered_otp}, Session OTP: {session_otp}")

        if entered_otp and session_otp and entered_otp == session_otp:  # Check if OTP matches
            request.session['otp_verified'] = True  # Mark OTP as verified
            return redirect('reset_password')  # Redirect to the reset password page
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'tasks/verify_otp.html')


# View for Reset Password
def reset_password(request):
    if request.method == "POST":
        email = request.session.get('reset_email', None)  # Get the email stored during OTP verification
        new_password = request.POST.get('new_password')

        # Debugging: Check if email exists in the session
        print(f"Email from session: {email}")

        if email is None:
            messages.error(request, "Email not found. Please start the process again.")
            return redirect('forgot_password')  # Redirect to the forgot password page

        try:
            user = User.objects.get(email__iexact=email)  # Case-insensitive email lookup
            user.set_password(new_password)  # Set the new password
            user.save()

            # Clear session data related to the reset process
            del request.session['reset_email']
            del request.session['reset_otp']

            messages.success(request, "Password reset successful! Please log in.")
            return redirect('login')  # Redirect to login page
        except User.DoesNotExist:
            messages.error(request, "No user found with this email. Please try again.")
            return redirect('forgot_password')

    return render(request, 'tasks/reset_password.html')


@login_required
def update_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)  # Ensures a 404 if no profile exists
    if request.method == 'POST':
        profile.photo = request.FILES.get('photo', profile.photo)
        profile.mobile_number = request.POST.get('mobile_number', profile.mobile_number)
        profile.address = request.POST.get('address', profile.address)
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    return render(request, 'tasks/profile.html', {'profile': profile})

# tasks/views.py
@login_required
def feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text')
        star_rating = request.POST.get('star_rating')

        # Save feedback
        Feedback.objects.create(user=request.user, feedback_text=feedback_text, star_rating=star_rating)
        messages.success(request, "Thank you for your feedback!")
        return redirect('feedback')

    # Fetch user's feedback
    feedbacks = Feedback.objects.filter(user=request.user).order_by('-created_at')
    star_ratings = range(1, 6)  # Pass the range of star ratings
    return render(request, 'tasks/feedback.html', {'feedbacks': feedbacks, 'star_ratings': star_ratings})

# tasks/views.py


@user_passes_test(lambda u: u.is_staff)  # Restrict access to admin users only
def admin_feedback(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        Feedback.objects.filter(id=feedback_id).delete()
        messages.success(request, "Feedback has been deleted.")
        return redirect('admin_feedback')

    # Fetch all feedback
    all_feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'tasks/admin_feedback.html', {'all_feedbacks': all_feedbacks})
