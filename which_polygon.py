
def which_polygon(points, gdf, name_col = 'name', lat_col = 'latitude', lon_col = 'longitude'):
  '''
  points:   A Pandas DataFrame with the points that you want to 
            cross reference against your polygons
            
  gdf:      A GeoPandas DataFrame with your polygons. Must have
            a 'geometry' column.
            
  name_col  The column in the the GDF which contains the name of
            the polygon which will be returned.
            
            
  lat_col   The name of the column containing latitude values
  
  lon_col   The name of the column containing longitude values
  '''
  
  # Function to check if one point remains within another
  def find_poly(point):
    # Iterate through each point if it falls within a polgon in the geodataframe 
    for k, r in gdf.iterrows():
      if point.within(r['geometry']):
        return r[name_col]
        break

    # Otherwise return nan if nothing fits
    return np.nan

  points['which_polygon'] = points.apply(lambda row: find_poly(
    # Create a point geom and pass if to which poly
    Point(row[lon_col], row[lat_col])) 
    # However, if there is no long/lat, simply return nan
    if pd.isnull(r[lon_col]) == False 
    else np.nan, axis = 1)

  return points['which_polygon']

