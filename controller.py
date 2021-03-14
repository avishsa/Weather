def get_data(res,query_components):
    res_data = b"missing parameters"
    if("lon" in query_components and "lat" in query_components):
        lon =query_components["lon"]
        lat = query_components["lat"]
        res_data = bytes(f'get_data {lon} {lat}','utf-8')
    res.send_response(200)
    # self.send_header()
    res.end_headers()
    res.wfile.write(res_data)



def get_summerize(res,query_components):
    res_data = b"missing parameters"
    if ("lon" in query_components and "lat" in query_components):
        lon = query_components["lon"]
        lat = query_components["lat"]
        res_data = bytes(f'get_summerize {lon} {lat}', 'utf-8')
    res.send_response(200)
    # self.send_header()
    res.end_headers()
    res.wfile.write(res_data)