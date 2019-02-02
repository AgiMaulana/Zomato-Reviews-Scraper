# zomato-reviews-scraper

## Install selenium
`pip install -r requirements.txt`

## Install Chrome Web Driver
Download latest Chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads <br /> <br />
Or if you on Linux/Ubuntu <br />
`wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip` <br /> <br />
Extract the binary then move to `/usr/bin/` <br />
`sudo mv chromedriver /usr/bin/chromedriver` <br />
`sudo chown root:root /usr/bin/chromedriver` <br />
`sudo chmod +x /usr/bin/chromedriver` <br /> <br />


## Run
add your target restaurant Zomato reviews page by add the URL to `urls.txt` <br />
then <br />
`python main.py`

# Lisence
This project is under the [MIT Lisence](https://github.com/AgiMaulana/instagram-comments-scraper/blob/master/LICENSE.md)
