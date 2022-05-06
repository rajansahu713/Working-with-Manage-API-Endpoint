from os import getenv
import requests
import json
import urllib
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
import xml.etree.ElementTree as ET

app = Flask(__name__)
api = Api(app)

class AddressDetails(Resource):
    
    def post(self):
        url = "https://maps.googleapis.com/maps/api/geocode"
        output_format = request.json["output_format"]
        
        if output_format == "json":
            parameters = {
                "address": request.json['address'],
                "key": getenv("AUTH_KEY")
            }
            
            base_url = f"{url}/{output_format}?"
            r  = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
            
            data = json.loads(r.content)
            response = {
                "coordinates":data.get('results')[0].get('geometry').get("location"),
                "address": data.get('results')[0].get("formatted_address")
            }
            
        
            return jsonify(response)
            
            
        elif output_format == "xml":
            url = "https://maps.googleapis.com/maps/api/geocode"
            
            parameters = {
                "address": request.json['address'],
                "key": getenv("AUTH_KEY")
            }

            base_url = f"{url}/{output_format}?"
            r  = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
            

            response_xml_as_string = r.content
            root = ET.fromstring(response_xml_as_string)
            address = root.find('result').find('formatted_address')
    
            coordinate_longitude = root.find('result').find('geometry').find('location').find('lng')
            coordinate_latitude = root.find('result').find('geometry').find('location').find('lat')
            
            root = ET.Element("root")
            doc = ET.SubElement(root, "address").text = address.text

            coor_long = ET.SubElement(root, "coordinate")
            ET.SubElement(coor_long, "lng").text = coordinate_longitude.text
            ET.SubElement(coor_long, "lat").text = coordinate_latitude.text
        
            xmlDoc= ET.tostring(root, encoding="unicode")

            return Response(xmlDoc, mimetype='text/xml')

        else:
            return "Invalid output format",400

        

    
api.add_resource(AddressDetails, '/getAddressDetails')

if __name__ == '__main__':
    app.run(debug=True)