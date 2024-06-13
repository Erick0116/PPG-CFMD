import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def vehicles_populate():
  return app_tables.vehicles.search()

@anvil.server.callable
def search_vehicles(query):
  results = app_tables.vehicles.search(plate_no=query)
  return results

@anvil.server.callable
def view_details(search_plateno):
  if search_plateno:
    results = app_tables.vehicles.search(plate_no=search_plateno)
    if results:
      return {'make': results[0]['make']}
  return None