# Restaurant Cleaning Tasks App

This is a web application built with Flask to manage restaurant details and associated cleaning tasks.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

The Restaurant Cleaning Tasks App is designed to help you manage restaurant information and associated cleaning tasks efficiently. It provides a user-friendly interface for adding restaurants, specifying cleaning tasks, and viewing upcoming cleaning schedules.

## Features

- **Add Restaurant:** Enter restaurant details, including name and location.
- **Specify Cleaning Tasks:** Define cleaning areas and their frequencies (Daily, Weekly, Monthly, Every 2 Days).
- **View Cleaning Schedule:** See upcoming cleaning dates and days remaining until the next clean.
- **Responsive Design:** The application is designed to work well on various devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/restaurant-cleaning-tasks.git
   ```

2. Navigate to the project directory:

   ```bash
   cd restaurant-cleaning-tasks
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.

## Dependencies

- Flask
- pymongo
- bson
- dateutil

You can install these dependencies using the provided `requirements.txt` file.

## License

This project is licensed under the [MIT License](LICENSE).