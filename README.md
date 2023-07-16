## One Piece Devil Fruit Finder

This project consists of an API and a frontend application that provide information about the Devil Fruits from the One Piece anime series. The API scrapes data from the One Piece wiki to gather details about the different devil fruits and exposes two endpoints to access this information.

## App diagram
![devil_fruit_diagram](https://github.com/manumafe98/One-Piece-Devil-Fruit-Finder-FastApi-MongoDb/assets/95315128/490450d2-3aae-465e-91a6-4d0ee4f50892)

## API

The API is built using FastApi and Docker, offers the following endpoints:

- `GET /devil_fruits`: Retrieves a list of all devil fruits available.
- `POST /devil_fruits`: Creates a new devil fruit and add it to the database.
- `GET /devil_fruits/<devil_fruit>`: Retrieves the details of a specific devil fruit selected by the user.
- `DELETE /devil_fruits/<devil_fruit>`: Deletes a specific devil fruit.
- `PUT /devil_fruits/<devil_fruit>`: Updates all the information of a devil fruit.
- `PATCH /devil_fruits/<devil_fruit>`: Updates one attribute of the specified devil fruit.

The API utilizes a Mongodb database to store the scraped data, enabling efficient retrieval of information
## Frontend Application

The frontend application is designed to consume the APIs `GET /devil_fruits/<devil_fruit>` endpoint. It features a user-friendly browser that allows users to search for devil fruits. When a fruit is searched, the application displays a card containing the fruit's image and its characteristics.

Both the API and the frontend application are containerized using Docker, making it easy to deploy and manage the project in various environments.

It uses the `POST /devil_fruits` endpoint with the `ADD` button on the navbar, so you can add your favorite fruits.

And with the `Update` button it consumes the `PATCH /devil_fruits/<devil_fruit>` endpoint, so you can modify the attributes of the fruit you want.

## Installation and Usage

First clone the repository, then if you don't have docker install it for your proper os.

Then execute the following command on the path of your cloned repository

```commandline
docker compose up -d
```

After that you can check your `localhost:8888` and `localhost:8000/devil_fruits` on your browser.
