# Pizza Website

Backlogg: https://docs.google.com/spreadsheets/d/131Dxy4QplduNJaxo41rS0nOelqbk0bQTxoG1y0TOsho/edit#gid=0

Website: https://fantastic4group.gitlab.io/pizza-website
**(GitLab pages is used to host this website)**

# Coding Conventions
**Spaces:** 4
<br>
**Comments:** English, space between `//` and the comment, capitalized.
<br>
**Namngivning:** Engelska, Klasser med storbokstav (UpperCamelCase)
<br>
**Variable naming:** CSS/HTML: kebab-case, JS: camelCase, classes: UpperCamelCase, Python: snake_case
<br>
**HTML/CSS:** Only use inline CSS with JavaScript actions.

# Programming Languages
HTML 5
<br>
CSS 3
<br>
Javascript (ECMAScript 2018)
<br>
Python 3.8.2

# Development environment
**Editor** - Personal preference
<br>

**Version Control Host** - GitLab
<br>
**OS** - WSL/Ubuntu
<br>
**Browsers** - Firefox
<br>
**Tests** - Python selenium library with the unreleased version 4
<br>
**Static validation** - HTML Validator, CSS Validator
<br>
**Documentation** - English
<br>
**Git Branches** 
- Branch names should use kebab-case.
- Needs to be approved by at least 2 members of the group, besides the marge request creator.

**Git Command Reference** - https://about.gitlab.com/images/press/git-cheat-sheet.pdf

# Definition of Done
+ Approved by the group, both and code structure. All code needs to follow the standards we have in place.
+ Get feedback from group members.
+ Tests should be green.
+ The code shall be documented.
+ Everyone in the group shall understand the code.
+ Allt ska vara presenterbart.
+ Everything shall be presentable. (If it's frontend)
+ All documents shall cover the whole sprint.

# Compiling
**Compile the website**
1. First you need to install the dependencies with the following commands: (if `firefox-esr` does not exist on your distro, use `firefox`)
```bash
apt update && sudo apt upgrade && sudo apt install -yqq curl jq sudo firefox-esr ruby-full build-essential zlib1g-dev
gem install jekyll bundler jekyll-less therubyracer
```
1. With the dependencies installed, to compile/run the website you can run:
```bash
# To compile the website
jekyll build -s site -d public
# To compile and run webserver
jekyll serve -s site -d public -P 8080
```

# Test Documentation
**How to run the tests**
1. Jekyll needs to compile the code.
1. A webserver needs to run the directory containing the compiled site, this can be done with jekyll, or with `python3 -m http.server --directory=public`. (What webserver you use does not matter)
1. Go to the tests folder, `cd tests/webtests`
1. Install required dependencies with `pip3 install selenium==4.0.0a6.post2 requests`
1. Now simply run `python3 -m unittest`


**How to add a new test**
1. Head to the tests directory with `cd tests/webtests`
1. Here you can create a new file with the name prefix `test_` (e.g `test_example.py`)
1. Inside your file you can create a test with this template:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
class ExampleTest(WebTestBase):
    def test_example(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
```
1. When you save this file you can simply run all tests with `python3 -m unittest` or to run a specific with `python3 -m unittest test_example`

# Automatic screenshots
1. Run a webserver like described earlier in this document.
1. Go to the folder `tests` and run `./screenshots.py`
1. The script will then create a new folder called `screenshots` containing the different pages with different resolutions, including full pages.

# Static validation
1. Compile the website as described earlier. (No need to run it)
1. Run the following commands to validate CSS and HTML:
```bash
./tests/validators/css_validator.sh public
./tests/validators/html_validator.sh public
```
# CI/CD
CI/CD will run all these tests and validations automatically before deploying, please refer to the [.gitlab-ci.yml](.gitlab-ci.yml) file for more information.

# Various licenses this project use  
- Fonts are from Google Fonts.
- All images are either from the owner or Unsplash.
