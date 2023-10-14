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

## Getting the API Key

To access weather data, this project uses the WeatherAPI service. To get an API key, follow these steps:

1. Visit the WeatherAPI website at [https://www.weatherapi.com/](https://www.weatherapi.com/).

2. Sign up for an account or log in if you already have one.

3. Once you are logged in, navigate to your account settings or dashboard.

4. Look for an option to create a new API key or access your existing API keys.

5. Generate a new API key. Some services may require you to subscribe to a specific plan or verify your email address to get access.

6. After generating the key, make sure to copy it to your clipboard or save it in a secure location.Now open view.py file in home folder,then in the function get_weather_data in place of<API_KEY> paste your api key

**Important**: Keep your API key secure. Do not share it publicly or expose it in your codebase. You can use environment variables or configuration files to store and access your API key securely.


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
