[![linter](https://github.com/Polyrom/python-project-52/actions/workflows/linter.yml/badge.svg)](https://github.com/Polyrom/python-project-52/actions/workflows/linter.yml) [![Actions Status](https://github.com/Polyrom/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Polyrom/python-project-52/actions) [![tests](https://github.com/Polyrom/python-project-52/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/python-project-52/actions/workflows/tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/e5c2320447804790f1ba/maintainability)](https://codeclimate.com/github/Polyrom/python-project-52/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e5c2320447804790f1ba/test_coverage)](https://codeclimate.com/github/Polyrom/python-project-52/test_coverage)
# Task manager
## Web app to easily manage tasks for your team

#### Choose an executive for your task, add priority status and necessary labels. All features can be customized to meet your needs!

### Feel free to visit the page, sign up and play around!

### [Demo on Railway](https://python-project-52-production.up.railway.app/) (Deprecated)

### Installation
1. Clone the repository
```
git clone https://github.com/Polyrom/python-project-52
cd python-project-52
```
2. Install dependencies with **Poetry**

    2.1. If you don't have Poetry, here's the installation guide:
         **[Poetry installation](https://python-poetry.org/docs/)**
```
make install
```
3. Create an .env file
```
touch .env
```
4. Populate the .env file with the following values:
```
DEBUG=True
SECRET_KEY=your_Django_secret_key (may be generated with 'make secretkey' command)
ACCESS_TOKEN=your Rollbar access token (optional)
```

5. Finish installation
```
make makemigrations
make migrate
make createsuperuser
```
6. Now can run the app on you localhost
```
make start
```
