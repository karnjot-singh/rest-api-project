# REST API Project MCDA5550
A Rest API Project using Django framework to make use of rest-framework to create APIs for hotels and reservations.

## Setup the Project
1. Clone this project on your computer.
2. Change the database configurations in ./hotelreservation/.env file.
3. Open ./hotelreservation directory in your editor.
4. At ./hotelreservation directorty run the following commands-
```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
```

## Following are the APIs available and their expected inputs/outputs
1. /api/hotel
  This API endpoint is used to create new hotel and fetch details of exisiting hotels.
  - Make a POST request to create a new hotel<br>
  >Input for this API is
  ```
  {
    "name": "Halifax Inn",
    "description": "Free Breakfast",
    "availability": "true",
    "phone_number": "9876543210",
    "city": "Halifax",
    "price": "130"
  }
  ```
  > Output will be
  ```
  Status Code - 201 
  {
    "id": 1,
    "name": "Halifax Inn",
    "description": "Free Breakfast",
    "availability": true,
    "phone_number": "9876543210",
    "city": "Halifax",
    "price": 130
}
  ```
  - Make a GET request to fetch exisiting hotels details
  > Output will be
  ```
  Status Code - 200
  [
    {
        "id": 1,
        "name": "Halifax Inn",
        "description": "Free Breakfast",
        "availability": true,
        "phone_number": "9876543210",
        "city": "Halifax",
        "price": 130
    },
    ....
  ]
  ```
