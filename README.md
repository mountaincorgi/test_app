# Test App

### Build

* Open the project in VS Code
* Make sure you have the Docker and Remote Development extensions installed
* Press F1 and select "Dev Containers: Rebuild and Reopen in Container"

### Custom Build

* This project is set up to run Django, Redis (as a cache and result backend), and RabbitMQ (as a message broker)
* All images and configuration for containers are specified in docker-compose.yaml. Modify the file if you want a different set of conatiners i.e. if you want postgres, pgAdmin, etc.
* Test new libraries and features in a new branch

### Tasks

* Celery tasks can be defined in your own apps, or if you go to testapp/jobs/tasks there are already a few tasks set up
* Run Celery tasks from the Django shell using `Task.apply_async()` or `Task.delay()`
* Make sure the Redis and RabbitMQ containers are running otherwise nothing will happen.

### Starting the Web Server and Celery

* This project uses VS Code launch configurations (see .vscode/launch.json)
* You and add or modify the existing configurations
* On the activity bar, go to the "Run and Debug" tab
* Select "Django" or "Celery" from the dropdown menu and click the play button
* This will execute the command defined in the launch configuration

### Notes

* Check the ports!
* Superuser: root/root
