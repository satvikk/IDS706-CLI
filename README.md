[![Python application](https://github.com/satvikk/IDS706-CLI/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/satvikk/IDS706-CLI/actions/workflows/python-app.yml)

# IDS706-CLI  

# checkifup  

This is a Command-Line-Interface that contains 2 commands within it. The url command checks if a url is responsive, or a website is working. The concept command checks if a concept is something that is literally above you. Feel free to submit pull requests to add more concepts which should be "up"

To run through docker:

```console
foo:~$ cd PATH/TO/IDS706-CLI
foo:/PATH/TO/IDS706-CLI$ docker build -t imagename .
foo:/PATH/TO/IDS706-CLI$ docker run imagename url http://satvikkishore.com
foo:/PATH/TO/IDS706-CLI$ docker run imagename concept stratosphere
```
