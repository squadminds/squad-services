# squad-services

There are 3 seperate Projects in this Repo.


Admin Interface -> This is the own version of Admin intrface. All the models and Users are handled but with a more customized 
and flexible approach. It uses the AdminLTE for the styling which is a free, Opensource Admin Inteface built on top of 
Bootstrap. It uses bootstrap row,column classes to make itself the prsentable to the smaller screens. 

API -> Rather than presenting the front end with Templates and other Files using Djngo, This project makes use of Django-REST-
Framework (DRF) to send and receive data using jSon objects. API endpoints are exposed for the data consumption. Authentication
mechanism is implemented using the django-auth and CORS problem is solved by  using django-cors-headers package.

Frontend -> To give the front end a more customized and very flexible approach, we have used seperate HTML pages rather than
django templates to GET,POST,PUT ( DELETE is not authorized and implemented on purpose) data via using AJAX , jQuery, javaScript , CSS and HTML. It gives the benifit of running a seperate server and a more fascinating page HTML by using the data only presentd by the API



