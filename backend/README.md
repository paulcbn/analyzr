
# Analyzr backend

## Architecture

Backend stack: Django + Django REST Framework

The django main **project** is called `/backend`

Inside there are 4 django **apps** and the django **project** configuration:  

1. `/backend/api_core` - main **app** made to be the entrypoint and the manager of all the other apps.  
It is also responsible with declaring the main entities used throughout the project. (eg. User, DoctorProfile)
2. `/backend/api_auth` - auth **app** that contains the auth logic and exposes the authentication endpoints
3. `/backend/api_doctor` - **app** that contains the doctor page logic and exposes the correspondent endpoints 
4. `/backend/api_patient` - **app** that contains the patient page logic and exposes the correspondent endpoints
5. `/backend/backend` - django **project** configuration 

Some important configuration lives in the `/backend/.env` file. To get the development going, you should copy it from `/backend/.env.example`.  
