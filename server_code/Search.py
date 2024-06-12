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
def view_details(query):
  results = app_tables.vehicles.search()
  if query:
    filtered_results  = [
      {
        'make': x['make'],
        'body_type':  x['body_type'],
        'color': x['color'],
        'model':  x['model'],
        'register_name': x['register_name'],
        'plate_no': x['plate_no'],
        'engine_no':  x['chasis_no'],
        'area_assigned':  x['area_assigned'],
        'status':  x['status'],
        'cr_no': x['cr_no'],
        'date_cr': x['date_cr'],
        'or_no':  x['or_no'],
        'date_renewed_or': x['date_renewed_or'],
        'next_renewal': x['next_renewal'],
        'insurance_type': x['insurance_type'],
        'insurance_name': x['insurance_name'],
        'premium': x['premium'],
        'coverage': x['coverage'],
        'expiry': x['expiry'],
        'remarks': x['remarks']
      }
      for x in results
      if query in x['plate_no']
    ]
    if filtered_results:
      return filtered_results[0]
    else:
      return None
  else:
    return None
  