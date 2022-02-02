

# Aura developer portal Web UI Automation

End-To-End Web Testing Selenium, Pytest

Architectural pattern - Page Object.

Browsers used: Chrome, Firefox, Edge (Edge in progress).

Ready for running in Github Actions. Configuration file is located in .gihub/workflows

For running locally you need  Python 4, browsers and requirement packages installed.

Structure:

Page objects located in /pages folder, test-functions located in /tests. 
conftest.py file contains fixtures used for tests.
settings.py file used for storing URL's, constants, helping methods.  

# Requirements: 

- Knowledge of Python syntax, data-types, OOP
- Knowledge of Selenium framework
- Knowledge of Pytest testing framework
- Understanding of Page Object pattern.

Helpful links in the description.

##How to write a test:


**1)** Remember:


End-to-end testing (E2E testing) refers to a software testing method that involves testing an application's workflow from beginning to end. This method aims to replicate real user scenarios so that the system can be validated for integration and data integrity.


**2)** Determine what you want to test. For example, user login scenario 


**3)** Create a page object file in the "pages" folder if you don't have it already. E.g "login_page.py"

   It will contain methods for interacting with this page.

**4)** Create a Class (e.g LoginPage) and inherit from the base_page class. 


**5)** Create a methods which will perform needed actions.

   E.g "def create_new_user(self, user_name, user_password):"

**6)** Add needed methods in Page's class to interact with this page
e.g def user_login():
        ...

**7)** While writing a code, add locators you need to Locators class in the same page object file (e.g class LoginPageLocators)

**8)** Create a test file in the tests folder using existed examples.

The name of the file should start from "test_" E.g "test_login_page.py"

**9)** Import needed pages. Write test functions in the test file. 

   Name of functions should start from "test_"

   ####Rules: 

1) inside the function determine the page which you want to manipulate:

    page = LoginPage()

2) Perform needed actions for test

    page.user_login()
    ...

4) Add assert statement to the end of the test. E.g "assert result == 1"


###Executing:


Pytest collects tests from '/tests' directory. Execute command: 'pytest'

**Run only 1 file with tests: pytest test_1.py**

**Run only 1 test: pytest test_1.py::test_one**

**Run test by its name: -k - pytest -k test_name**

Example command:

pytest -v --disable-warnings --browser=chrome --headless=on --screenshot=on --screenshot_path=on \
--html=report.html --junit-xml=junit/test-results-chrome.xml --reruns 3 -n 2

This will run pytest in verbose mode (-v) with disabled warnings, in Chrome with headless mode, 
screenshot will be saved if test failed, html and junit reports will be saved, if test failed - rerun it 3 times (--reruns),
in parallel mode (-n 2) where 2 is amount of browser instances in the same time (N max = amount of CPU'S)

###Run arguments:



-v = verbose mode

-m [mark_name] = run only marked tests. You can mark test with: 

"@pytest.mark.name" fixture before test. Existed marks are in pytest.ini file. 

-s = string output

for rerunning failure tests  --reruns [number_reruns]. E.g pytest --reruns 3 will rerun failed test 3 times.

for other arguments use pytest documentation. To add your own argument use conftest.py file.  

----------------------------------------------------------


**Pytest traceback settings:**


**pytest --showlocals** # show local variables in tracebacks


**pytest -l**           # show local variables (shortcut)


**pytest --tb=auto**    # (default) 'long' tracebacks for the first and last


**pytest --tb=long**    # exhaustive, informative traceback formatting


**pytest --tb=short**   # shorter traceback format


**pytest --tb=line**    # only one line per failure


**pytest --tb=native**  # Python standard library formatting


**pytest --tb=no**      # no traceback at all



The **-r** flag can be used to display a “short test summary info” at the end of the test session

To create result files which can be read by Jenkins, Gitlab or other Continuous integration servers, use this invocation:

**-- pytest --junitxml=path**

----------------------------------------------------------   

##Useful links and best practices:

Selenium webdriver:

https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/


Pytest:

https://docs.pytest.org/


Page Object pattern - getting started:

https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests


Using Selenium With Python in a Docker Container:

https://nander.cc/using-selenium-within-a-docker-container  


UI Automation best practices:

https://www.blazemeter.com/blog/top-15-ui-test-automation-best-practices-you-should-follow/

