# Foursquare Feeds

A python script that will generate an iCal (`.ics`) feed of your checkins on [Foursquare][4sq]/[Swarm][swarm]. If you set it up to save this file to a publicly-visible location on a webserver, and run the script regularly, you can subscribe to the feed in your favourite calendar application.

Foursquare [used to have such feeds][feeds] but they've stopped working for me.
[I wrote a bit about this.][blog]

[4sq]: https://foursquare.com
[swarm]: https://www.swarmapp.com
[feeds]: https://foursquare.com/feeds/
[blog]: https://www.gyford.com/phil/writing/2019/05/13/foursquare-swarm-ical-feed/


## Installation


### 1. Make a Foursquare app

Go to https://foursquare.com/developers/apps and create a new App.


### 2. Install python requirements

Either using [pipenv](https://pipenv.readthedocs.io/en/latest/):

    $ pipenv install

or [pip](https://pip.pypa.io/en/stable/):

    $ pip install -r requirements.txt


### 3. Set up config file

Copy `config_example.ini` to `config.ini`. Change the `IcsFilepath` to wherever you want your file to be saved.

To get the `AccessToken` for your Foursquare app, you will have to go through the laborious procedure in step 4...


### 4. Get an access token

On https://foursquare.com/developers/apps, in your app, set the Redirect URI to `http://localhost:8000/`

In a terminal window, open a python shell:

    $ python

and, using your app's Client ID and Client Secret in place of `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` enter this:

```python
import foursquare
client = foursquare.Foursquare(client_id='YOUR_CLIENT_ID' client_secret='YOUR_CLIENT_SECRET', redirect_uri='http://localhost:8000')
client.oauth.auth_url()
```

This will output something like:

    'https://foursquare.com/oauth2/authenticate?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2F'

Copy the URL from your terminal *without the surrounding quotes* and paste it into a web browser.

Your browser should redirect to a URL like the one below, with an error about not being able to connect to the server (unless you have a webserver running locally on your machine):

    http://localhost:8000/?code=XX_CODE_RETURNED_IN_REDIRECT_XX#_=_

Copy the code represented by `XX_CODE_RETURNED_IN_REDIRECT_XX` (note that there may be an extra `#_=_` on the end which *you should not copy*).

Back in your python shell, with that code, enter this, replacing
`XX_CODE_RETURNED_IN_REDIRECT_XX` with the code you just copied:

```python
client.oauth.get_token('XX_CODE_RETURNED_IN_REDIRECT_XX')
```

This will output another long code, which is your Access Token.

Enter this in your `config.ini`.

## Run the script

You're ready to go:

    $ ./generate_feeds.py

This should create an `.ics` file containing up to 250 of your most recent
checkins (see `--all` argument below to get more).

If the file is generated in a location on your website that's publicly-visible, you should be able to subscribe to it from a calendar application. Then run the script periodically to have it update.

Note that the file might contain private checkins or information you don't want to be public. In which case, it's probably best to make the name of any such publicly-readable file very obscure.

### Script options

#### `--all`

By default the script only fetches the most recent 250 checkins. To fetch ALL checkins add the `--all` flag:

```bash
$ ./generate_feeds.py --all
```

Depending on how many checkins you have you might only want to run it with
`--all` the first time and, once that's imported into a calendar application,
subsequently only fetch recent checkins.

#### `-v` or `--verbose`

By default the script will only output text if something goes wrong. To get
brief output use `-v` or `--verbose`:

```bash
$ ./generate_feeds.py -v
Fetched 250 checkins from the API
Generated calendar file ./mycalendar.ics
```

If fetching `--all` checkins then increasing the verbosity with another `-v`
will show more info than the above:

```bash
$ ./generate_feeds.py -vv --all
5746 checkins to fetch
Fetched checkins 1-250
Fetched checkins 251-500
[etc...]
Fetched checkins 5501-5750
Fetched 5744 checkins from the API
Generated calendar file ./mycalendar.ics
```

(No I don't know why it fetched 2 fewer checkins than it says I have.)


## About

By Phil Gyford  
phil@gyford.com  
https://www.gyford.com  
https://github.com/philgyford/foursquare-feeds

