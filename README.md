# instagram-clone
# Author
  Annet Khavere  
  
# Description  
This is an  Instagram clone where people share their  images and videos for other users to view, like and comment.
Users can sign up, login, view and post photos, search and follow other users.
##  Live Link  
 Click [View Site](lagram.herokuapp.com/)  to visit the site
 
## User Story  
  
* Sign in to the application to start using.  
* Upload pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on their timeline.  
  

  
## Setup and Installation   
  
##### Cloning the repository:  
 ```bash 
(https://github.com/anneyk/instagram-clone.git)
```
##### Navigate into the folder
 ```bash 
cd instagram-clone
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations  
 ```bash 
python manage.py makemigrations gram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* Python3.6
* Django
* Heroku


## License 

* MIT  
* Copyright (c) 2022 **Annet Khavere**
