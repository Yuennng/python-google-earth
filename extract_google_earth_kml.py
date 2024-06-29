def extract_google_earth_kml(folder_path):
    '''
        Extracts important data from kml files exported from Google Earth Pro
        
        input:
            1. folder_path: (string) folder path storing all the kml files
        output:
            1. area_name: (list) name of the placemarks
            2. long: (list) longitude of the placemarks
            3. lat: (list) latitude of the placemarks
            4. addr: (list) address of the placemarks
            5. link: (list) url of the placemark
    '''
    area_name = []
    long = []
    lat = []
    addr = []
    link = []
    
    for root, dirs, file in os.walk(folder_path): # walk through directory tree
        for f in file:
            if '.kml' in f:
                with open(root + "/" + f) as data:
                    kml_soup = BeautifulSoup(data, 'lxml-xml') # Parse as XML
                    
                out = kml_soup.find_all('Placemark')
                for o in out:
                    area_name.extend([o.find('name').text])
                    longlong, latlat, _ = o.find('coordinates').text.split(",")
                    long.extend([longlong])
                    lat.extend([latlat])
                    addr.extend([o.find('address').text])
                    link.extend([Soup(o.find('description').text,'html.parser').find('script').text.split('"')[1]])

    return area_name, long, lat, addr, link