# Notch Coding Challenge 

This coding challenge requires the creation of an endpoint that saves/retrieves historical events.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install
```

## Usage

```python
python manage.py runserver
```

## About the endpoint

The endpoint ``/event/manage`` has two HTTP request methods.

```
POST - to save an event. 
GET  - to retrieve events (using field filters)
```

### Business Logic
  
- In this application, as the complexity grows, there needs to be an additional layer for the business validations and other rules. 
- The additional layer is called Business Service Layer - that stores validation logic which is referenced by the controller handler. 
- In our application, this is in the file `event/service.py`. Each Service class is a representation and handler of a **Schema**. (Event in our case)
- **Helper** classes can also be used in the future when there are generic functions.  


### Testing 

- The source code consists of test cases to validate creation, retrieval and filtering of events. 
- Other tests on GET request to ``event/manage`` can include:  
    - Invalid date format.
    - Invalid filters such as component and environment values.
- Other tests on POST request to ``event/manage`` can include:
    - Invalid request body fields to create an event  
 
