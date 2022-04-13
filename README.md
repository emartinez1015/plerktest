# README #

This is a backend test for Plerk.io 

The following aspects will be evaluated in this test:

- Definition of data modeling
- ORM management
- Optimization and code cleanup
- Test solution


### Run Application ###

* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py loaddata users companies transactions`
* `python manage.py runserver`

### Test Endpoints ###

This application api has swagger fot test the endpoint

in this link https://medinson1015.pythonanywhere.com/swagger/ and you can see the api documentation in this link https://medinson1015.pythonanywhere.com/redoc/

Execute Token service with this credentials

```
email: plerk@plerk.mx
password: 123456
```

<img width="1289" alt="image" src="https://user-images.githubusercontent.com/2013300/163280936-58673c23-6152-48a7-8b02-edf1291895ac.png">


Copy access Token

<img width="1289" alt="image" src="https://user-images.githubusercontent.com/2013300/163281129-a254b9ef-84fc-4987-9941-c059d6f4a6d9.png">

Paste the token in the Authorize dialog window. Don't forget to put the word `Bearer` before the token


<img width="1289" alt="image" src="https://user-images.githubusercontent.com/2013300/163281696-de92116c-e83e-4140-803f-4fcb4ab27c10.png">



