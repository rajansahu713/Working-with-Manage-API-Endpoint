<h2> In this Application we are using google Geolocation API.
We will made a request to the API and get the location coordinates.</h1>


`Run the application`

```python
python app.py
```
`CASE 1: JSON`

```json
{
"address": "# 3582,13 G Main Road,4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "json"
}
```
`Output:`

```json
{
"address": "3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru,
Karnataka 560008, India",
"coordinates": {
"lat": 12.9658286,
"lng": 77.63948169999999
}
}
```
`CASE 2: XML`
```json
{
"address": "# 3582,13 G Main Road,4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "xml"
}
```
`Output:`
```xml
<root>
<address>3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru,
Karnataka 560008, India</address>
<coordinate>
<lng>77.6394817</lng>
<lat>12.9658286</lat>
</coordinate>
</root>
```
`CASE 3: Other than XML and JSON`
```json
{
"address": "# 3582,13 G Main Road,4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "sxms"
}
```
`Output:`
```json
"Invalid output format"
```

## References:
https://developers.google.com/maps/documentation/geocoding/start