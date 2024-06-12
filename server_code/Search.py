import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def vehicles_populate():
  return app_tables.vehicles.search()

@anvil.server.callable
def search_vehicles(query):
  results = app_tables.vehicles.search(plate_no=query)
  return results

@anvil.server.callable
def view_details(search_plateno):
  results = app_tables.vehicles.search()
  return results
 # print("Search Results:", results)
  #if results and len(results) > 0:
   # first_result = results[0]
   # return [first_result['make'], first_result['body_type'], first_result['color'], first_result['plate_no']]
  #else:
   # return None