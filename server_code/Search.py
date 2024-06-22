import anvil.users
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
def search_history(query):
  results = app_tables.transferhistory.search(plate_no=query)
  return results

@anvil.server.callable
def search_repair(query):
  results = app_tables.repairapproval.search(plate_no=query)
  return results

@anvil.server.callable
def view_details(search_plateno):
  if search_plateno:
    results = app_tables.vehicles.search(plate_no=search_plateno)
    if results:
      return {
        'make': results[0]['make']
      }
  return None

@anvil.server.callable
def get_next_id():
  all_ids = app_tables.partsitem.search()
  if all_ids:
    max_id_no = max((record['id'] for record in all_ids if record['id'] is not None), default=0)
    next_id_no = max_id_no + 1
  else:
    next_id_no = 1
  return next_id_no

@anvil.server.callable
def parts_item_populate(plate_no, date):
  return app_tables.partsitem.search(plate_no=plate_no, date=date)

@anvil.server.callable
def history_populate():
  return app_tables.transferhistory.search()

@anvil.server.callable
def repair_populate():
  return app_tables.repairapproval.search(status="Requested")