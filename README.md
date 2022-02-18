# SeleniumPython
This project automates few flows from https://the-internet.herokuapp.com/ using selenium 3.141.0. The user can either run the tests on the localhost or saucelabs (Account credentials should be configured)

How to run the tests:
- Download the project and configure it in pycharm
- Use a virtual env which is of python 3.10.0 version
- Install dependencies using the command pip install -r requirements.txt
- Execute the following command from the terminal

To run the tests on localhost:
python -m pytest -n auto --browser=chrome --host=localhost

To run the tests on saucelabs:
python -m pytest -n auto --browser=chrome --host=saucelabs

To run the tests on saucelabs tunnel:
python -m pytest -n auto --browser=chrome --host=saucelabs-tunnel

Note : Using the option '-n auto' launches tests in parallel mode and you will see multiple browser sessions launching at the same time
