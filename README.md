# EC2 Instance Starter

A very basic Django app to start already-created EC2 instances when needed.  Handy for "Desktop" instances that are mostly powered off but are needed periodically by users who don't have IAM credentials of their own.  At some point I would like to add SAML support, but currently authentication is handled purely in Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

You need Python (3.5) and virtualenv to get started. Further requirements are in requirements.txt (eg boto3, Django)

### Installing

Create and activate a virtual environment with virtualenv
```
cd ec2manager
virtualenv env
.\env\Scripts\activate
```
or on Linux:
`source env/bin/activate`

Create an IAM user that only has permission to describe and power on instances ([Example policy](../master/exampleIAMpolicy.json)) and either use `aws configure` or set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

```
pip install -r requirements
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details

## Acknowledgments

* Thanks to [Russell Ballestrini](https://github.com/russellballestrini/), whose function I used for creating a dictionary of tags
