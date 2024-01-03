# Support Onboarding - Automate

This is the first module technical assignment for Support Onboarding - Automate

### Problem Statement: 

Go to [StackDemo](https://bstackdemo.com/) and performs the following steps (note - use this script for all subsequent tasks):

- Sign in as user “demouser”
- Add iPhone 12 to cart
- Check out & submit a shipping address
- Verify “Your Order has been successfully placed.” text successfully appears on the page

### Prerequisites
```
python3 and pip3 should be installed
```

### Steps to run test session

- Clone the repository
```
git clone https://github.com/Kavisha-340/module-technical-assignment-1.git
cd module-technical-assignment-1
```
- Install the required dependencies
```
# create virtual environment
python3 -m venv env
source env/bin/activate
# install the required packages
pip3 install -r requirements.txt
```
- Update your credentials in .env file
```dotenv
BROWSERSTACK_USERNAME="BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY="BROWSERSTACK_ACCESS_KEY"
URL="https://hub.browserstack.com/wd/hub"
```

- Run tests

  a. For single
  ```
  python3 ./scripts/single.py
  ```
  b. For parallel
  ```
  python3 ./scripts/parallel.py
  ```
