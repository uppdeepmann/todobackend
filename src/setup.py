from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["Django==1.8",
                          "django-cors-headers==1.1.0",
                          "djangorestframework==3.3.0",
                          "mysqlclient==1.4.2.post1",
                          "uwsgi==2.0",
                          "protobuf==3.7.1",
                          "six==1.12.0",
	                  "mysql-connector-python==8.0.15",
                          			  
 
			    			  ],
  extras_require       = {
                            "test": [
                              "colorama==0.4.1",
                              "coverage==4.0.3",
                              "django-nose==1.4.2",
                              "nose==1.3.7",
                              "pinocchio==0.4.2"
                            ]
                         }
)
