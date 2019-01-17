# iReporter

 [![Build Status](https://travis-ci.org/mderek227/iReporter-api.svg?branch=api)](https://travis-ci.org/mderek227/iReporter-api) [![Coverage Status](https://coveralls.io/repos/github/mderek227/iReporter-api/badge.svg?branch=api)](https://coveralls.io/github/mderek227/iReporter-api?branch=api) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/55c30326bca466d990d32aabd8a2158)](https://www.codacy.com/app/mderek227/iReporter-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mderek227/iReporter-api&amp;utm_campaign=Badge_Grade)

## About

iReporter enables citizens to report any form of corruption to the appropriate authorities. Users can also alert government on things that need intervention.

## Features

- Users can create an account and log in

- Users can create a red-flag record

- Users can create intervention record 

- Users can edit their red-flag or intervention records

- Users can delete their red-flag or intervention records

- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records

- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records

- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved)

- Users can add images to their red-flag or intervention records

- Users can add videos to their red-flag or intervention records

## Getting Started

Clone the project from this [link](https://github.com/mderek227/iReporter-api)

## Prerequisites

* A computer with an operating system (Linux, MacOS or Windows can do the job)
  Python 3.6
* Pytest or any other preffered python tesing tool
* Postman to test the API endpoints
* A preffered text editor
* Git to keep track of the different project branches

## Installing

Clone the project from this [link](https://github.com/mderek227/iReporter-api)

Open your terminal or command prompt for windows users

Type

```
$ cd ireporter
$ git checkout ft-API
$ virtualenv venv
$ pip install -r requirements.txt
$ python run.py
```

## Deployment

The API is hosted on Heroku. Use the link below to navigate to it.

[heroku](https://xxxx.herokuapp.com/)

## Testing the Api

Run the command below to install pytest in your virtual environment

`$ pip install pytest`

Run the tests

`$ pytest -v`

## Endpoints

| Endpoint          | Functionality |
| --------          |     --------- |
| `GET /api/v1/incidents` | Fetch all incident records |
| `GET /api/v1/incidents/<incident_id>` | Fetch a specific incident record |
| `DELETE /api/v1/incidents/<incident_id>` | Delete a specific incident record |
| `PATCH /api/v1/incidents/<incident_id>/location` | Edit incident record's location |
| `PATCH /api/v1/incidents/<incident_id>/comment` | Edit incident record's comment |
| `PATCH /api/v1/incidents/<incident_id>/status` | Change incident record's status |
| `POST /api/v1/incidents` | Create an incident record |
| `POST /api/v1/users` | Create user account |
| `POST /api/v1/users/admin` | Create admin account |
| `POST /api/v1/users/login` | Login user or admin |

## Built With

 Python 3.6.5
 Flask (A python microframework)

## Tools Used

* Pylint
* Pytest
* Virtual environment

## Author

Derrick Mananu


## Acknowledgements

Thanks to God who enabled me to this point