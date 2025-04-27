# To-Do-List - Task Management Application

To-Do-List is a robust task management system built with Django that helps users organize and track their tasks efficiently. The application provides features for task creation, management, completion tracking, and user feedback.

## Features

- **User Authentication**
  - Secure registration and login system
  - Profile management with customizable details
  - Profile picture upload capability

- **Task Management**
  - Create new tasks with title, description, and due date
  - View tasks in different categories (To-Do, Completed)
  - Edit task details and status
  - Archive or delete completed tasks

- **User Interface**
  - Clean and responsive design
  - Intuitive navigation
  - Mobile-friendly layout

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.9 or higher
- Django 4.0 or higher
- SQLite (included with Python)

## Project Structure

```
TO DO LIST/
├── to_do_list/           # Main project directory
│   ├── venv/            # Virtual environment directory
│   ├── tasks/           # Main application folder
│   │   ├── __init__.py
│   │   ├── admin.py    # Admin panel configurations
│   │   ├── apps.py     # App configuration
│   │   ├── models.py   # Database models
│   │   ├── views.py    # View logic
│   │   ├── urls.py     # App-specific URLs
│   │   └── templates/  # HTML templates
│   │       └── tasks/  # All templates stored in this location
│   │           ├── base.html
│   │           ├── create_task.html
│   │           ├── todo_tasks.html
│   │           ├── completed_tasks.html
│   │           ├── login.html
│   │           └── profile.html
│   ├── my_anydo/       # Project configuration folder
│   │   ├── __init__.py
│   │   ├── settings.py # Project settings
│   │   ├── urls.py     # Global URL routing
│   │   └── wsgi.py     # WSGI configuration
│   ├── static/         # Static files (CSS, JS, Images)
│   ├── media/         # User uploaded files
│   ├── db.sqlite3     # SQLite database
│   └── manage.py      # Django management script
└── README.md          # Project documentation
```

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/arjuntanil/To-Do-List.git
   cd to_do_list
   ```

2. **Create a Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser 
   #if needed
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your web browser and navigate to: `http://127.0.0.1:8000`
   - Admin panel can be accessed at: `http://127.0.0.1:8000/admin`

## Template Locations

- **Base Template**: `tasks/templates/tasks/base.html`
  - Contains the main layout and navigation
  
- **Task Templates**:
  - Create Task: `tasks/templates/tasks/create_task.html`
  - Todo Tasks: `tasks/templates/tasks/todo_tasks.html`
  - Completed Tasks: `tasks/templates/tasks/completed_tasks.html`
  
- **User Templates**:
  - Login/Register: `tasks/templates/tasks/login.html`
  - Profile: `tasks/templates/tasks/profile.html`

## Usage

1. **Registration/Login**
   - Create a new account or login with existing credentials
   - Update your profile with additional information

2. **Task Management**
   - Click "Create Task" to add a new task
   - View all tasks on the dashboard
   - Mark tasks as completed
   - Edit task details using the edit button
   - Delete tasks when no longer needed

3. **Profile Management**
   - Access your profile through the navigation menu
   - Update personal information
   - Upload a profile picture

## Additional Features

1. **Task Status Tracking**
   - Visual indicators for task status
   - Separate views for todo and completed tasks

2. **Responsive Design**
   - Mobile-friendly interface
   - Adaptive layout for different screen sizes

3. **User Experience**
   - Intuitive navigation
   - Clean and modern interface
   - Easy task management

- Secure file uploads

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
