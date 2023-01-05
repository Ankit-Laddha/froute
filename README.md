# froute
is a python script/parser that fetches and shows google maps route for a destination from various pre-defined locations

## Motivation
While house-hunting in berlin, I always want to check how far is the new house I'm applying for is from the places which I visit very frequently e.g. office, Alexanderplatz, etc And what are the transport options from that place.

To do so, I end up opening multiple tabs of google maps, checking the new house address from those predefined places. This is annoying and time-wasting (atleast for me).

With froute, I simply pass the new-house address and it gives me all that information (BEST ROUTE, LESS WALKING ROUTE, along with time required) with one command.

# Pre-requisite

## Installation required
- python, pip3, 
- library: os, googlemaps, sys
```bash
pip3 install <library-name>
```

## Warning for Google Maps API usage
```text
Under the free plan, you are allowed up to 100,000 requests per 24 hours, and up to 2,500 requests* per day per user. If you exceed these limits, you will be prompted to enable billing on your project, and you will be charged according to the pricing listed on the Google Maps Platform website.

*PLEASE REFER OFFICIAL GOOGLE WEBSITE FOR UPDATED AND ACCURATE INFORMATION (Google Maps API pricing page)[https://developers.google.com/maps/pricing-and-plans/]
```

## Setup

### MAPS API KEY
Create and get API key for Google Maps API.
Google Maps API allows you to display maps on your website and/or application, and customize the maps with your own content. To use the Google Maps API, you need to sign up for an API key. Here is a general outline of the steps you need to follow to use the Google Maps API:

```text
Steps:
1. Go to the Google Cloud Console.
2. Click the project drop-down and select or create the project for which you want to add an API key.
3. Click the hamburger menu and select APIs & Services > Credentials.
4. On the Credentials page, click Create credentials > API key.
5. The API key created dialog displays your newly created API key.
6. Click Close.
7. The new API key is listed on the Credentials page under API keys.
```
[Google Cloud Console](https://console.cloud.google.com/getting-started)

Recommended:
Restrict your API key to avoid unauthorized access.
```text
Steps:
1. Click the Edit button for the API key that you want to secure.
2. In the Key restriction section, set Application restrictions to IP address.
3. Add IP Addresses where you mostly going to use this script.
4. Click Save.
```

### BILLLING ACCOUNT
In order to use the Google Maps API, you need to set up a billing account with Google Cloud. The Google Maps API is a paid service, and you need to enable billing with a credit card in order to use the API.

```text
Steps:

1. Go to the (Google Cloud Console)[https://console.cloud.google.com/getting-started].
2. Click the project drop-down and select or create the project for which you want to enable billing.
3. Click the hamburger menu and select Billing.
4. Click the Add billing account button.
5. Follow the prompts to set up a new billing account.
6. Once you have set up a billing account, you will be able to use the Google Maps API in your project. You can view your API usage and usage limits in the Google Cloud Console. You can also set up alerts to notify you when you are approaching your usage limits.

You can find more information about pricing and usage limits for the Google Maps API on the (Google Maps API pricing page)[https://developers.google.com/maps/pricing-and-plans/].
```
[Google Maps API pricing page](https://developers.google.com/maps/pricing-and-plans/)

### Store API key
Now store your Maps api-key as your system environment variable. 
```bash
export GOOGLE_MAPS_API_KEY=<Your-API-Key>
```

### Update your pre-defined places
Update your places in this line
https://github.com/Ankit-Laddha/froute/blob/9d9d00724d16f7756ecff8eecf42a90f4a3c2bac/froute.py#L24

## Usage
```python
py froute.py "<Add your address here>"
```

## Example 

Request:
```text
py froute.py "Grindelwaldweg 9, 13407 Berlin"
```
Response:
```text
START_ADDRESS: Grindelwaldweg 9, 13407 Berlin

DESTINATION:    Delivery Hero SE, Oranienburger Straße, Berlin
BEST_ROUTE:     120 | Bus towards S+U Hauptbahnhof | Stops: 5 | Stop At: U Seestraße | (7 mins) --->
                U6 | Subway towards Alt-Mariendorf | Stops: 6 | Stop At: U Oranienburger Tor | (7 mins) --->
                Walk to Oranienburger Str. 70, 10117 Berlin, Germany(7 mins) --->
                 == 21 mins

DESTINATION:    Delivery Hero SE, Oranienburger Straße, Berlin
LESS_WALKING:   120 | Bus towards S+U Wittenau -> Bus 220 | Stops: 10 | Stop At: U Wittenau | (11 mins) --->
                220 | Bus towards Frohnau, Hainbuchenstr. | Stops: 1 | Stop At: Göschenplatz/S Wittenau (Berlin) | (1 min) --->
                Walk to Wittenau(2 mins) --->
                S1 | Commuter train towards S Wannsee Bhf (Berlin) | Stops: 8 | Stop At: Oranienburger Straße | (18 mins) --->
                Walk to Oranienburger Str. 70, 10117 Berlin, Germany(1 min) --->
                 == 33 mins

===================================================================================================
DESTINATION:    Alexanderplatz Berlin
BEST_ROUTE:     Walk to Residenzstr(13 mins) --->
                U8 | Subway towards Hermannstraße | Stops: 9 | Stop At: Alexanderplatz | (15 mins) --->
                Walk to 10178 Berlin, Germany(1 min) --->
                 == 29 mins

DESTINATION:    Alexanderplatz Berlin
LESS_WALKING:   120 | Bus towards S+U Wittenau -> Bus 220 | Stops: 4 | Stop At: Paracelsus-Bad | (5 mins) --->
                U8 | Subway towards Hermannstraße | Stops: 10 | Stop At: Alexanderplatz | (16 mins) --->
                Walk to 10178 Berlin, Germany(1 min) --->
                 == 22 mins

===================================================================================================
DESTINATION:    Berlin Zoological Garden, 10787 Berlin
BEST_ROUTE:     120 | Bus towards S+U Hauptbahnhof | Stops: 7 | Stop At: Leopoldplatz | (10 mins) --->
                U9 | Subway towards S+U Rathaus Steglitz | Stops: 6 | Stop At: Berlin Zoologischer Garten railway station | (9 mins) --->
                Walk to Hardenbergpl. 8, 10787 Berlin, Germany(3 mins) --->
                 == 22 mins

DESTINATION:    Berlin Zoological Garden, 10787 Berlin
LESS_WALKING:   120 | Bus towards S+U Hauptbahnhof | Stops: 7 | Stop At: Leopoldplatz | (10 mins) --->
                U9 | Subway towards S+U Rathaus Steglitz | Stops: 6 | Stop At: Berlin Zoologischer Garten railway station | (9 mins) --->
                Walk to Hardenbergpl. 8, 10787 Berlin, Germany(3 mins) --->
                 == 22 mins

===================================================================================================


```

## Future probable enhancement ideas 
- Not planned. Current implementation serves my purpose. But maybe for time when I'm bored and want to work on something ;)
```text
[ ] Do a check on my current account usage for maps API and exit if usage is going to exceed to avoid any extra charges.
[ ] Convert it to a CLI with ability to store some state. So people can add/edit/remove existing saved addresses.
[ ] Show top 3 nearby supermarket with distance and transport options
[ ] Show alternate routes also
[ ] Show output in a MAP format instead of plain text
[ ] ...
```
