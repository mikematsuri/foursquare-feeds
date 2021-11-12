#!/usr/bin/env python

import foursquare
import os

FOURSQUARE_CLIENT_ID=os.getenv('FOURSQUARE_CLIENT_ID')
FOURSQUARE_CLIENT_SECRET=os.getenv('FOURSQUARE_CLIENT_SECRET')
FOURSQUARE_INTERMEDIATE_CODE=os.getenv('FOURSQUARE_INTERMEDIATE_CODE')
print(FOURSQUARE_INTERMEDIATE_CODE)
client = foursquare.Foursquare(client_id=FOURSQUARE_CLIENT_ID, client_secret=FOURSQUARE_CLIENT_SECRET, redirect_uri='http://localhost:8000')
res = client.oauth.auth_url()
print(res)
res = client.oauth.get_token(FOURSQUARE_INTERMEDIATE_CODE)
print(res)

