# aSpend

This project is a work in progress, aiming to create a financial tracking interface using Flask and Bootstrap. What sets it apart from other financial trackers is its focus on:

* Multi-currency support
* Flexible dashboard customization on the main page
* Advanced budget planning capabilities

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technologies](#technologies)

## Installation

To clone the repository and install dependencies, run the following commands:

```bash
git clone https://github.com/Vanilara/Sadok.git
cd sadok
pip install -r requirements.txt
python3 remake_database.py
python3 -m flask run --debug --port=5001
```


## Usage
Before registration, users will see a demo layout of the interface. After logging in, they will access a dashboard where they can purchase collected data using their balance. User information can be found at /admin.

## Configuration

Before running the project, you need to set up the `.env` file. Example configuration file:

# .env
```
DEBUG_MODE=True/False
SERVER_URL=For debug mode when DEBUG_MODE=False (https://example.com)
```

## Technologies
* Python 3.10
* Flask 3.x
* Bootstrap
* jQuery