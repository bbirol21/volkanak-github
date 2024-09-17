from flask import Flask, render_template, url_for
from azure.storage.blob import BlobServiceClient

import csv
import io

app = Flask(__name__)

#Azure Blob Storage Configuration
connection_string = "DefaultEndpointsProtocol=https;AccountName=bartubirolsdocuments123;AccountKey=lGufKaiFanZWbpaSiKQJk53c/Wxd13ChrIqSJ8h1ghtiImB20i1GQXvYRPB8TTyuxCZrvl2Zvtex+AStjcdUZw==;EndpointSuffix=core.windows.net"
container_name = "bartubirolscontainer"
blob_name = "customers.csv"

def load_csv_data_from_blob():
    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Get the container client
    container_client = blob_service_client.get_container_client(container_name)
    
    # Get the blob client (the file you want to download)
    blob_client = container_client.get_blob_client(blob_name)
    
    # Download the blob (file) as a stream
    download_stream = blob_client.download_blob()
    
    # Read the content of the stream and decode as needed (CSV in this case)
    csv_content = download_stream.readall().decode('utf-8')
    
    # Use csv.reader to parse the CSV data
    myList = []
    numbers_data = csv.reader(io.StringIO(csv_content), delimiter=',')
    next(numbers_data)  # Skip the header
    for row in numbers_data:
        myList.append(row)
    
    return myList


def load_csv_data(filename):
    myList = []
    with open(filename) as customers:
        numbers_data = csv.reader(customers, delimiter=',')
        next(numbers_data) #skip the header
        for row in numbers_data:
            myList.append(row)
        return myList
    

@app.route('/')
def index():
    #new_list = load_csv_data('customers.csv')
    new_list = load_csv_data_from_blob()
    return str(new_list)
    #return "Hello World Bartu22222 github"
    #return render_template('index.html')

if __name__ == "_main_":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug = True)

#during the production you should set the debug to False