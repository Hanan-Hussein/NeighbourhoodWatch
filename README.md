#  Neighbourhood Watch
### By Hanan Hussein
### [Live Site](https://watchneighbourhood.herokuapp.com/) 

![Screenshot from 2022-06-21 09-22-31](https://user-images.githubusercontent.com/36597096/174730612-1555faeb-f986-4e35-a505-4b6196fd7089.png)



## Description 
This is a site where users can submit their projects, rate projects by usability,content and design, view and edit their profiles.
The site also provides api to view all projects and the users in the system
## Behavioural Driven Development
1. A user can sign up
2. A user can login
3. A user can post their projects for rating
4. A user can rate projects
5. A user can view projects
6. A user can view voters and their rates
7. An api to fetch all users in the system
8. A user can view and edit profile
9. An api to view all projects in the site

## Installation

    # clone the repository
    $ git clone https://github.com/Hanan-Hussein/NeighbourhoodWatch
    $ cd NeighbourhoodWatch
    # Open with your favourite code editor
    $ for vscode 
    $ code .
    
    
### Create a virtualenv and activate it

    $ python3 -m venv env
    $ . env/bin/activate

### Or on Windows cmd

    $ py -3 -m venv env
    $ env\Scripts\activate.bat

### Install dependancies in the app

    $ python3 -m install -r requirements.txt 
    
 ### Run 
 
     $ python3 manage.py runserver
     
 ### Built With
* Python 3.10.4
* Django
* psql
* JS

## License
Copyright (c) 2022 Hanan-Hussein
[MIT LICENSE](https://github.com/Hanan-Hussein/NeighbourhoodWatch/blob/master/LICENSE)
