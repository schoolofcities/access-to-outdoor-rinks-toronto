import requests

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, you'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = { "id": "ttc-routes-and-schedules"}
package = requests.get(url, params = params).json()

# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):

# To get metadata for non datastore_active resources:
    if not resource["datastore_active"]:
        url = base_url + "/api/3/action/resource_show?id=" + resource["id"]
        resource_metadata = requests.get(url).json()
        url = resource_metadata["result"]["url"]
        print(resource_metadata)
        # From here, you can use the "url" attribute to download this file

import requests, zipfile, io

#Download data with API
r = requests.get(url)
with open (r"data/TTC/gtfs.zip", mode="wb") as file:
    file.write(r.content)

#Extract gtfs zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("analysis/data/ttc")