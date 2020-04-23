NOTE: PINBOARD.IN NOW FILTERS TWITTER LINKS OUT OF POPULAR. THIS PROJECT IS HERE FOR REFERENCE, ONLY.

[No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

If you want to read tweets that are popular on [pinboard](http://pinboard.in), but don't want to sift through the other links, this is for you.

Requirements
------------

- [Python 3](https://www.python.org)
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
- [Requests](http://docs.python-requests.org/en/master/)


Usage
-----
1. From the terminal in the directory of the files, run <code>python3 -m venv ENV</code> to create the virtual environment.
2. <code>source env/bin/activate</code> to run the environment.
3. <code>pip install beautifulsoup4</code> to install the first dependency.
4. <code>pip install requests</code> to install the second dependency.
5. Run `python grab.py`, to create `output.html`. Open `output.html` in your web browser. If you want to open `output.html` from the terminal, use `open output.html` (*nix) or `explorer output.html` (Windows).
