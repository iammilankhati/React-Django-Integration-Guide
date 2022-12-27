Please follow the steps before using this django backend template

1. in myapp/middleware.py set the domain to redirect
2. tinymce editor is added through admin.py, make sure tinyInject.js is included
   under build/static file in production (keep tinyInject.js in static folder in
   BASE_DIR , so whenever build file changes copy the tinyInject.js to
   build/static/tinyInject.js)

# What I did here

1. Setting up react build files for template
2. Installed whitenoise and set paths for static files for serving.
3. Redirected http to https in prouduction
4. disable the api end points in production
5. tinymce editor is added through models, make sure tinyInject.js is included
   under build/static file in production

# Production settings

1. place the build file of react in BASE_DIR
2. select the backend folder and compress to zip file
3. Upload the zip file into the python app created folder in cpanel
4. extract the zip file the BASE_DIR, so that all the files lies in BASE_DIR,
   but not in backend folder in c cpanel
5. from the python app, run pip install requirements.txt
6. Copy the snippets from python app and go to terminal
7. Paste the code and run.

   # python manage.py makemgirations

   # python manage.py migrate

   # python manage.py collectstatic

   # python manage.py check --deploy
