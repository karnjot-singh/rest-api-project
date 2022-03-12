# REST API Project MCDA5550
A Rest API Project using Django framework to make use of rest-framework to create APIs for hotels and reservations.

## Setup the Project
1. Clone this project on your computer.
2. Change the database configurations in ./hotelreservation/.env file. This project uses MySQL if you use another database then settings.py file should be updated accordingly.
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
2. /api/makereservation
  This API endpoint is used to make a new reservation for existing hotel.
  - Make a POST request to make a new reservation<br>
  >Input for this API is (NOTE hotel_name should be present in database)
  ```
  { "hotel_name": "Halifax Inn", 
  "checkin": "2022-03-18", 
  "checkout": "2022-03-19", 
  "guests_list": [  
           { "guest_name" : "Guest one", 
             "gender": "M" 
           },
           { "guest_name" : "Guest two", 
             "gender": "f" 
           },
           ...
       ] 
  } 
  ```
  > Output will be
  ```
  Status Code - 200
  {
    "confirmation_number": "Hal000001"
}
  ```
  - Make a GET request to fetch all reservation details
  > Output will be
  ```
  Status Code - 200
  [
    {
        "id": 1,
        "hotel": 1,
        "confirmation_number": "Hal000001",
        "check_in": "2022-03-18",
        "check_out": "2022-03-19",
        "guest_list": [
            {
                "id": 1,
                "name": "Guest one",
                "gender": "M"
            },
            {
                "id": 2,
                "name": "Guest two",
                "gender": "f"
            },
            ...
        ]
    },
    ...
  ]
  ```
