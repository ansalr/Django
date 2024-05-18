install    -->  pip install virtualenv
create     -->  python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
activate   -->  venv\Scripts\activate
deactivate -->  deactivate


Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate

command to migrate model
    python manage.py migrate

make migration after creating the models
    python manage.py makemigrations

    after every migration we need to migrate 
    python manage.py migrate

create login credencial to login admin:
    python manage.py createsuperuser

    username : ansalr
    email: ansalr@email.com
    pass: ansal@123


    username: test01
    pass: ansal@01

to connect models 

connect models to admin file


register:
    admin.site.register(Room)


query data from database:
    variablename = "modelname".object.all()
    variablename = "modelname".object.get()
    variablename = "modelname".object.filter()
    variablename = "modelname".object.exclude()
    variablename = "modelname".object.create()

query data in djangoshell:

    Product.objects.all().order_by("?").first()
    Product.objects.all().order_by("?").last()


    