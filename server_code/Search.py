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
  