# assignment3

This is a home improvement tool sharing application that is used for ISQA 8210 assignment3. This application uses mailgun. You'll need your own credentials to send emails. Adding API information is done in https://github.com/abpadan/assignment3/blob/main/tms/toolms/tools/views.py within lines 39-40. 

**Local**
    
    git clone git@github.com:abpadan/assignment3.git
    cd assignment3/tms/toolms/
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver


