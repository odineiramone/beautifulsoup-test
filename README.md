# Beautiful Soup test

A test with using urllib to get html content, Beautiful Soup to "read" it and flask to send data via REST API. My target is status of the subway and train services from Sao Paulo, Brazil

## Made with

  - Python 3.6.4 :snake:
  - Flask

## Setup

  - Use Python 3 (highly recommended use [asdf](https://github.com/asdf-vm/asdf) to manage python versions)

  -  Create new environment
    ```bash
    python3 -m venv env
    ```
  -  Activate environment
  ```bash
  source env/bin/activate
  ```
  -  Install dependencies
  ```bash
  pip3 install -r requirements.txt
  ```

## Run

  - Run
  ```bash
  python3 app.py
  ```

  - By curl in your terminal
  ```
  curl http://127.0.0.1:5000/status
  ```

  - or access in your browser
  ```
  http://127.0.0.1:5000/status
  ```

<div align="center">
  <img src="https://media.giphy.com/media/xTiTnHvXHHxOTcdmxO/giphy.gif" alt="Nice project!"/>
</div>
