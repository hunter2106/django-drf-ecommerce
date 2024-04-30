<!-- To start the Project initially (One - Time - Use) -->
   <!-- To Create Virtual-Environment (Consider Virtual-Environment as a box inside which we will use the tech stack accordingly) -->
        python -m virtualenv DRF-eComm/venv

   <!-- To start the Project initially (It creates all the necessary BoilerPlates) -->
        django-admin startproject drfecomm

   <!-- To install/update django to the latest version -->
        pip install django


<!-- To go/open the Terminal in the Virtual-Environment -->
    source venv/bin/activate


<!-- To run the server -->
    ./manage.py runserver


<!-- To get random-secret-key -->
   <!-- First open shell -->
        python manage.py shell
   
   <!-- Type and import from following -->
        from django.core.management.utils import get_random_secret_key

   <!-- Print the random-secret-key inside the shell to get it -->
        print(get_random_secret_key())


<!-- To create environment variables we install package python-dotenv (environment variables are created for another layer of security such that not anybody can access those variables except the devs) -->
     pip install python-dotenv


<!-- Intall Django-REST Framework -->
     pip install djangorestframework


<!-- Install pytest (for testing the project along-side devolpment) -->
     pip install pytest