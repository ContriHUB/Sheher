# Sheher

An utility **Django WebApp** that uses Django packages.

### Features: 

+ Rating and Review
+ Complaint Portal
+ About Places
+ Username Generator
+ Safety Index Of Place


## Getting Started

## How to run locally?
* [Install Python](https://www.wikihow.com/Install-Python)
* Clone this repository
    ```
    git clone https://github.com/ContriHUB/Sheher.git
    ```
* Create Virtual Environment
    ```
    python -m venv <env_name>
    ```
* Activate the environment
    * On Windows, run: `<env_name>\Scripts\activate`
    * On Linux/Mac, run: `source <env_name>/bin/activate`    
* Install the dependencies
    ```
    pip install -r requirements
    ```
* Change directory to *Sheher*
    ```
    cd Sheher
    ```
* To train crime rate model change Directory to *home*
    ```
    cd home
    ```
* Train Crime Rate Model,
    ```
    python train_crimerate.py
    ```
* To apply the migrations run,
    ```
    python manage.py makemigrations
    ```
    
    ```
    python manage.py migrate
    ```
* Now to run the server, and visit `http://127.0.0.1:8000/`.
    ```
    python manage.py runserver
    ```
* To access admin panel, you need to be superuser. Follow [this](https://www.geeksforgeeks.org/how-to-create-superuser-in-django/) link for instructions.

For help getting started with Django, view [online documentation](https://docs.djangoproject.com/en/4.1/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

##### Steps to contribute - 
1. Fork this repo and clone it to your system.
2. Get the issue assigned to you on the [ContriHUB](https://sac.mnnit.ac.in/contrihub/) website. 
3. Make the required changes. Please keep your changes relevant only to the issue specified.
4. Add your name to [CONTRIBUTORS.md](CONTRIBUTORS.md).
5. Create a PR with your changes and a detailed description of the changes you have made. 
6. Submit the PR link on the ContriHUB website.

[_References_](https://github.com/ContriHUB/ContriHUB-23#reference-links)

## Contributors

A list of contributors can be found in [CONTRIBUTORS.md](CONTRIBUTORS.md).
