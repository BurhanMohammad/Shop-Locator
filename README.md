
# Shop Locator

This is a Django-based web application for storing and querying the locations of various shops based on their latitude and longitude coordinates.

## Installation

To run the application locally, follow these steps:

1.Clone the repository:

```bash
  https://github.com/BurhanMohammad/Shop-Locator.git
```

2.Change to the project directory: 

```bash
  cd django-shop-locator-app
```
3.Create a new virtual environment:

```bash
  python -m venv venv
```
4. Activate the virtual environment:

```bash
  source venv/bin/activate
```
5.Install the dependencies:

```bash
  pip install -r requirements.txt
```
6.Run the migrations: 

```bash
  python manage.py makemigrations
  python manage.py migrate
```

7.Create a superuser:

```bash
  python manage.py createsuperuser
```

8. Start the development server:

```bash
  python manage.py runserver
```

The application should now be running at http://localhost:8000.
## Features

### The application provides the following features:

- Create, Read, and Update operations for managing shops.
- A view for displaying a form with fields for the user to enter their current location (latitude and longitude) and a distance (in kilometers).
- When the form is submitted, the view queries the database for all shops within the specified distance from the user's location and displays the results in a template.



## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```


## Deployment

This application is designed to be deployed on Railway.app. To deploy the application on Railway.app, follow these steps:

- Fork the repository to your own GitHub account.
- Create a new project on Railway.app.
- Connect the project to your GitHub repository.
- Configure the deployment settings in Railway.app.
- The application should now be deployed and running on Railway.app.

## Acknowledgements

This project was inspired by a coding challenge from 91social.