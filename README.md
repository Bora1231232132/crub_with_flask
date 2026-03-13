# Flask Todo Task Manager

A simple and elegant web application for managing your daily tasks. Built with Flask and SQLAlchemy, this application allows you to create, view, update, and delete tasks with ease.

## Features

- ✅ **Create Tasks** - Add new tasks to your todo list
- ✅ **View Tasks** - Display all tasks sorted by creation date
- ✅ **Update Tasks** - Edit existing task content
- ✅ **Delete Tasks** - Remove completed or unwanted tasks
- 🎨 **SCSS Styling** - Modern and responsive design with SCSS stylesheets
- 💾 **Database Persistence** - Tasks are stored in SQLite database

## Technologies Used

- **Python 3.14** - Programming language
- **Flask 3.1.3** - Web framework
- **SQLAlchemy 2.0.48** - ORM (Object-Relational Mapping)
- **Flask-SQLAlchemy 3.1.1** - Flask integration with SQLAlchemy
- **Jinja2 3.1.6** - Template engine
- **SCSS/pyScss 1.4.0** - Stylesheet preprocessing
- **SQLite** - Lightweight database

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone or download this repository:**

   ```bash
   cd Flask_tutorial
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Getting Started

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**

   ```
   http://localhost:5000
   ```

3. **Start managing your tasks!**

## Project Structure

```
Flask_tutorial/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page (task list)
│   └── update.html      # Task edit page
├── static/              # Static files
│   ├── style.css        # Compiled CSS
│   └── style.scss       # SCSS stylesheet
├── instance/            # Instance folder
└── env/                 # Virtual environment (not tracked in version control)
```

## Routes

| Route          | Method | Description                  |
| -------------- | ------ | ---------------------------- |
| `/`            | `GET`  | Display all tasks            |
| `/`            | `POST` | Create a new task            |
| `/update/<id>` | `GET`  | Display update form for task |
| `/update/<id>` | `POST` | Update task content          |
| `/delete/<id>` | `GET`  | Delete a task                |

## Database Model

### MyTask

- **id** (Integer) - Primary key, unique identifier
- **content** (String) - Task description/content
- **competed** (Integer) - Task completion status (0 = pending, 1 = completed)
- **created** (DateTime) - Timestamp when task was created

## Usage Example

1. **Add a Task:**
   - Navigate to the home page
   - Enter task description in the input field
   - Click "Add Task" button

2. **View Tasks:**
   - All tasks are displayed on the home page
   - Tasks are sorted by creation date

3. **Update a Task:**
   - Click the "Update" button next to a task
   - Modify the task content
   - Click "Update Task" button

4. **Delete a Task:**
   - Click the "Delete" button next to a task
   - Task will be permanently removed

## Notes

- The database file (mydatabase.db) is created automatically on first run
- SCSS files are automatically compiled to CSS
- Debug mode is enabled, so changes to the code will automatically reload the application

## Future Enhancements

- Task completion status toggle
- Task priority levels
- Due dates for tasks
- User authentication
- Task categories/tags
- Data export functionality

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the comments in the source code or create an issue in your repository.
