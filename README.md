# inventory_api

## To get started

### 1. Clone the repository

```
git clone git@github.com:<username>/inventory_api.git
cd inventory_api
```

### 2. Setup Project

1. Install the virtualenv tool and create a virtual environment

```
pip install virtualenv
virtualenv env
```

2. Install the dependencies

```
pip install -r requirements.txt
```

3. Run the migrations

```
python manage.py makemigrations
python manage.py migrate
```

4. Finally, run the server

```
python manage.py runserver
```

### 3. How to use the API

#### Endpoints:

1. http:localhost:8000/box_list/: Returns the list of all boxes in the inventory

2. http:localhost:8000/create_box/: Allows staff users to add boxes to the inventory

3. http:localhost:8000/details/<id>/: Allows staff users to view one box at a time and update box details

4. http:localhost:8000/my_boxes/: Allows staff user to view boxes they created

5. http:localhost:8000/delete/<id>/: Allows the creator of the box to delete the information about the box from the database.

































