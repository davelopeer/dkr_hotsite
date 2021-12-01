# Drubchen de Khandro Sangdu Hotsite


Website for Dzongsar Khyentse Rinpoche visit to [Chagdud Gonpa Khadro Ling](https://chagdud.com.br/) event subscriptions.

![dkr](http://dharmalog.com/aloha/wp-content/uploads/dzongsar-j-khyentse-r-1024x578.jpg)
---
## Description

Dzongsar Khyentse Rinpoche is a great buddhist master that will come in december to Chagdud Gonpa Khadro Ling, in Três Coroas, Brazil.
For this event is expected hundreds of people to come and their subscription will need a particularly website, with different subscription forms.

## Requirements

* Python 3.6.4
* Pip

## Running 

1. Install all the project dependencies by running:

`pip install -r requirements.txt`

2. Open the file `env.example` and export all the required _ENVs_ with the proper values.

#### With docker

With docker it's as easy as can be. Just run:

```
./scripts/run-dev.sh upd
```

And access the portal in [localhost:8000](http://localhost:8000)

To stop the service, run:

```
./scripts/run-dev.sh down
```


## Forms URIs

The following URIs are available with the different subscription forms

- Health Form: [/health-form](http://localhost:8000/health-form/)
- Guest Form: [/guest-form](http://localhost:8000/guest-form/)
- Volunteer Form: [/volunteer-form](http://localhost:8000/volunteer-form/)
- Sponsor Form: [/sponsor](http://localhost:8000/sponsor/)
- Sponsored Form: [/sponsored-form](http://localhost:8000/healthsponsored-form/)
- Special Guest Form: [/special-guest](http://localhost:8000/special-guest/)
- Cancellation Policy: [/cancellation-policy](http://localhost:8000/cancellation-policy/)


## Author

[David Barenco](https://www.linkedin.com/in/david-barenco-7b84a012a/)



