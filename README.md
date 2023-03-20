# Library Service API
- An API service for library management, written in Django REST Framework

## Features
- Management of borrowings and book returns
- Books are automatically hidden, and it gets the status "out_of_books" when there's no copies of this book left.
- It is possible to create books with two types of covers - Hard and Soft.
- It is possible to filter borrows by status and customer (user) id.
- Supports JWT authentication.
- Swagger documentation.
- Telegram-support - you get an alert when new borrowing is created, and statistics about overdue borrowings every day (Celery).

## There are such endpoints:

### User:

- [POST] /users/register/   (register your user)
- [POST] /users/login/   (login your user)
- [GET] /users/me   (info about yourself)
- [PUT] /users/me   (update all info about yourself)
- [PATCH] /users/me  (partial update of info about yourself)
- [POST] /users/token (get your JWT token for access)
- [POST] /users/token/refresh (update your access token)

### Book :

- [POST] /api/library/books/   (create nem book)
- [GET] /api/library/books/   (list of all books)
- [GET] /api/library/books/{id}   (detail info about book)
- [PUT] /api/library/books/{id}   (update all book instance)
- [PATCH] /api/library/books/{id}   (partial update of book instance)
- [DELETE] /api/library/books/{id}   (delete book with chosen id)

### Borrows:

- [GET] /api/library/borrowings/   (list of all borrowings)
- [GET] /api/library/borrowings/{id}   (detail info about borrow)
- [PUT] /api/library/borrowings/{id}   (update all borrow instance)
- [PATCH] /api/library/borrowings/{id}   (partial update of borrow instance)
- [DELETE] /api/library/borrowings/{id}   (delete borrow with chosen id)
- [DELETE] /api/library/borrowings/{id}/return   (return book with given borrow id)

## How to run
Note: Requires Docker to be locally installed

- Copy this repo from github:
```git
git clone https://github.com/AnnaKabatova/library-service.git
```
- Create venv and activate it through terminal:
```git
python -m venv myvenv

#Windows activaition:
myvenv\Scripts\activate

#Unix or Linux activation:
source myvenv/bin/activate
```
- Copy .env.sample file, rename it to .env. Populate it with all required data.
- Run app via Docker through terminal:
```git
docker-compose up --build
```
- Create admin user & Create schedule for running sync in DB

## Pre-installed test users:
You can test this service by using pre-installed test users.
Admin:
```git
email: test_admin@admin.com
password: qwertyui
```
Ordinary user:
```git
email: test_user@user.com
password: 1q2w3e4r
```

## How to register:
- Create user at /api/user/register/ endpoint
- Get user token at /api/user/token/ endpoint
- Authorize with it on /api/doc/swagger/ or use ModHeader wtih Request header:
```
Header: Authorization
Value: Bearer <Your access token> 
```
