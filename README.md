# Lintshots

![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/RaymondBrien/ci-lintshots)


Lintshots is a simple automation tool to put all your python files in a repository
into the [Code Institute linting validator](https://pep8ci.herokuapp.com/), take a
screenshot of the results and save each file's screenshot with its relevant name
locally as a `.png` on your machine for documentation.

## Main components:

- Google Chrome Driver
- Selenium

> [!NOTE]
> You must already have google Chrome browser installed locally.

## Steps to Run Lintshots

1. **Install Chrome Driver**:
    - Download the appropriate Chrome Driver version for your Chrome
    browser from the [Chrome Driver website](https://sites.google.com/a/chromium.org/chromedriver/downloads) or directly [here](https://googlechromelabs.github.io/chrome-for-testing/)
    - Extract the downloaded file and move the chromedriver to a directory
    in your system's `PATH`. Alternatively, put in a common location and echo path.
    Set path as environment variable or directly in `screenshots.py`.

    For more information or to automate driver installs via cli:
    https://github.com/GoogleChromeLabs/chrome-for-testing#other-api-endpoints


2. **Set Up Virtual Environment and Install Dependencies**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate

    pip install -r requirements.txt
    ```

3. **Add env variables**:

    Here is where to include:
    - url of the repository you wish to use
    - github token if you have a large repo to avoid restrictions

4. **Run Lintshots**:
    ```sh
    python screenshots.py
    ```


### Extras:

x. **Optional: Customize File Naming**:
    - If you want to customize the naming convention for the screenshots, modify the `get_screenshot_filename()` function in the `screenshots.py` file.

x. **Optional: Customize Output Directory**:
    - If you want to save the screenshots in a different directory, modify the `OUTPUT_DIR` variable in the `screenshots.py` file.

x. **Optional: Customize File Extensions**:
     - If your Python files have a different file extension than `.py`, update the `PYTHON_FILE_EXTENSIONS` variable in the `screenshots.py` file to send to a different validator, ***IF*** the validator can grab the file content via a dynamic url.

x. **Optional: Customize Linting Delay**:
     - Change delay length between opening each Python file and taking the screenshot as needed for slower internet connections or for quicker results if you need. Modify the `LINTING_DELAY` variable in the `screenshots.py` file.


## Requirements breakdown:

<details>
<summary>Click to open</summary>

- attrs==24.2.0:

Purpose: attrs is a package for defining classes without boilerplate code.
Use Case: Used for creating classes with automatic attribute management, validation, and conversion.

- certifi==2024.7.4:

Purpose: Certifi provides Mozilla's CA Bundle in Python.
Use Case: Ensures that your Python applications can verify the SSL certificates of the servers they connect to.

- charset-normalizer==3.3.2:

Purpose: Charset-Normalizer is an alternative to chardet, used for detecting the encoding of text.
Use Case: Helps in handling text encoding issues, especially when dealing with various text data sources.

- h11==0.14.0:

Purpose: h11 is a pure-Python, high-performance HTTP/1.1 protocol library.
Use Case: Used for building HTTP clients and servers with a focus on performance and correctness.

- idna==3.7:

Purpose: IDNA is a library for handling Internationalized Domain Names in Applications (IDNA).
Use Case: Ensures proper handling of domain names containing non-ASCII characters.

- outcome==1.3.0.post0:

Purpose: Outcome is a small utility library for capturing the result of a computation.
Use Case: Used in asynchronous programming to handle the results of computations, whether they succeed or fail.

- PySocks==1.7.1:

Purpose: PySocks is a SOCKS proxy client for Python.
Use Case: Allows routing network traffic through a SOCKS proxy server.

- requests==2.32.3:

Purpose: Requests is a simple and elegant HTTP library for Python.
Use Case: Used for making HTTP requests to interact with web services and APIs.

- selenium==4.23.1:

Purpose: Selenium is a browser automation tool.
Use Case: Used for web scraping, testing web applications, and automating repetitive web tasks.

- sniffio==1.3.1:

Purpose: Sniffio is a small utility to detect which async library is currently running.
Use Case: Helps in writing code that works with multiple async libraries.

- sortedcontainers==2.4.0:

Purpose: SortedContainers is a pure-Python implementation of sorted list, sorted dict, and sorted set data structures.
Use Case: Provides efficient sorted collections for various use cases.

- trio==0.26.2:

Purpose: Trio is an async/await-native I/O library for Python.
Use Case: Used for writing asynchronous programs, particularly those that involve I/O operations.

- trio-websocket==0.11.1:

Purpose: Trio-WebSocket is a WebSocket library for Python built on top of Trio.
Use Case: Used for creating WebSocket clients and servers in an asynchronous manner using Trio.

- typing_extensions==4.12.2:

Purpose: Typing Extensions provides backports of new type system features to older Python versions.
Use Case: Ensures compatibility with newer type hints and features in older Python versions.

- urllib3==2.2.2:

Purpose: urllib3 is a powerful, user-friendly HTTP client for Python.
Use Case: Often used as a dependency for other HTTP libraries like requests, providing additional features and reliability.

- websocket-client==1.8.0:

Purpose: websocket-client is a WebSocket client for Python.
Use Case: Used for creating WebSocket clients to interact with WebSocket servers.

- wsproto==1.2.0:

Purpose: wsproto is a WebSocket protocol stack written in Python.
Use Case: Provides low-level WebSocket protocol handling, often used as a dependency for higher-level WebSocket libraries.

</details>