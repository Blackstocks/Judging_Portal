# Judging_Portal
Developed an innovative judging portal leveraging HTML, CSS, JavaScript, Django, and Google Docs, significantly streamlining the live judging process for large-scale competitions.


#Setting up the environment:


Open the project folder in VS Code and run the following to activate the virtual environment:
          virtualenv myenv
          myenv\Scripts\activate(Windows)
          source ./bin/activate(linux/MacOs)
          Pip install django
Change the directory to reg_portal by:
          cd portal
Install some modules
          pip install google
          pip install google-auth
          pip install google_api
          pip install jsonfield
          pip install google-api-python-client
Now you are in the Django project directory. You can run the following to start the server:
python manage.py runserver
File Structure:
.portal
├── customUser
|   └── handles the user models
├── dashboardJudge
|   └── handles the judge dashboard
├── dashboardPaarticipant
|   └── handles the participant dashboard
├── portal
|   └── project directory
└── scores
   └── handles the scores

Portal is the main project folder containing the settings.py
customUser has the CustomUser model that is an extension of the abstract user model of the django and also has two one to one models Participant and Judge.
Dashboard Judge takes care of the judge dashboard and all the functionality related to it. Same goes for the participant dashboard.
The scores app handles the scores and has score model and a few signals in signals.py to get the desired functionality.

Way of doing stuff:
Decorators have been used in various apps to restrict the views to authenticated user.
Signals have been used to automate some of the functionality upon triggering them.
All the urls are named as “judge _url” or “participant_url” depending on the app.
The functionality of  the dashboard pages are written in views and one could map to them using the urls.
The authentication and registration are handled by the customUser app itself. The url for participant and judge are different.
The otp is also handled by the VerifyOTP view of the customUser app and it uses ajax for that in the templates.
The scores app handles the core part of the project which is to get the functionality of judging portal. They create score row when a judge chooses to judge a participant and stores the data and then get the average score and stuff.
The participants are also assigned a rank and it gets updated every time a new score is created, by using signals.
The class names are generic and while styling access the class by using the whole structure for example, “.main .card .profile h4” in order to avoid issues.
All the styling is done by following responsive grid view.
The template folder in every app folder has the following structure and while accessing then to render in view, it goes as render(request, ‘appname/file.html’)
appname
└── templates
   └── appname
       └── file.html

Functionality that needs to be added:
Integration of judging portal judging page with scores model.
And basic functionality of various other pages in the dashboard.
The design and implementation of various parts of dashboard of jude and participant dashboard.
Credentials:
Super User & Judge:
Username: abhinav
Password: 1729
Participant dashboard:
        Username: participant1
        Password: judging1234
