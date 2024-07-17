# Django Blog Application

This is a simple blog application built using Django and Django REST Framework. It includes basic CRUD functionalities for managing posts and comments, with token-based authentication for user access.

## Setup Instructions

### Prerequisites

- Python (3.6 or higher)
- Django
- Django REST Framework
- Git (optional, for cloning repository)

### Installation

1. **Clone the repository:**

   ```bash
   git clone  https://github.com/CODEr-SaNjU/Blogapp.git
   cd Blogapp
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv blogappvenv
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for accessing Django admin):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   The server will start running at `http://localhost:8000`.

## API Endpoints

### Posts

- **List all Posts**: `GET /api/posts/`

  Example Response:
  ```json
  [
    {
      "id": 1,
      "title": "First Post",
      "content": "This is the content of the first post.",
      "author": "admin",
      "published_date": "2024-07-25T10:00:00Z",
      "comments": [
        {
          "id": 1,
          "post": 1,
          "author": "user1",
          "text": "Nice post!",
          "created_date": "2024-07-25T12:00:00Z"
        },
        {
          "id": 2,
          "post": 1,
          "author": "user2",
          "text": "Great job!",
          "created_date": "2024-07-25T13:00:00Z"
        }
      ]
    },
    {
      "id": 2,
      "title": "Second Post",
      "content": "Content of the second post.",
      "author": "user1",
      "published_date": "2024-07-26T08:00:00Z",
      "comments": []
    }
  ]
  ```

- **Create a Post**: `POST /api/posts/`

  Example Request Body:
  ```json
  {
    "title": "New Post",
    "content": "This is the content of the new post."
  }
  ```

- **Retrieve a Post**: `GET /api/posts/<post_id>/`

  Example Response:
  ```json
  {
    "id": 1,
    "title": "First Post",
    "content": "This is the content of the first post.",
    "author": "admin",
    "published_date": "2024-07-25T10:00:00Z",
    "comments": [
      {
        "id": 1,
        "post": 1,
        "author": "user1",
        "text": "Nice post!",
        "created_date": "2024-07-25T12:00:00Z"
      },
      {
        "id": 2,
        "post": 1,
        "author": "user2",
        "text": "Great job!",
        "created_date": "2024-07-25T13:00:00Z"
      }
    ]
  }
  ```

- **Update a Post**: `PUT /api/posts/<post_id>/`

  Example Request Body:
  ```json
  {
    "title": "Updated Post Title",
    "content": "Updated content of the post."
  }
  ```

- **Delete a Post**: `DELETE /api/posts/<post_id>/`

### Comments

- **List all Comments for a Post**: `GET /api/posts/<post_id>/comments/`

  Example Response:
  ```json
  [
    {
      "id": 1,
      "post": 1,
      "author": "user1",
      "text": "Nice post!",
      "created_date": "2024-07-25T12:00:00Z"
    },
    {
      "id": 2,
      "post": 1,
      "author": "user2",
      "text": "Great job!",
      "created_date": "2024-07-25T13:00:00Z"
    }
  ]
  ```

- **Create a Comment for a Post**: `POST /api/posts/<post_id>/comments/`

  Example Request Body:
  ```json
  {
    "text": "This is a new comment."
  }
  ```


## Authors

- @coder-sanju
