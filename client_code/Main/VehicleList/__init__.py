from ._anvil_designer import VehicleListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import get_dom_node



class VehicleList(VehicleListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_vehicles.items  = anvil.server.call('vehicles_populate')
    self.expanded = False
    self.expandable_content.visible = False
   
    
  def toggle_expand(self, **event_args):
    if not self.expanded:
      self.expandable_content.visible = True
      self.expanded = True
      self.expand_button.icon = "fa:chevron-up"
    else:
      self.expandable_content.visible = False
      self.expanded = False
      self.expand_button.icon = "fa:chevron-down"
 

  def btn_search_click(self, **event_args):
    self.rp_vehicles.items  = anvil.server.call('search_vehicles', self.txt_search.text)
    search_plateno  = self.txt_search.text
    vehicle_record = app_tables.vehicles.search(plate_no=search_plateno)
    registration_record = app_tables.registration.search(plate_no=search_plateno)
    if vehicle_record and registration_record:
      self.txt_make.text = vehicle_record[0]['make']
      self.txt_bodytype.text = vehicle_record[0]['body_type']
      self.txt_color.text = vehicle_record[0]['color']
      self.txt_area.text = vehicle_record[0]['area_assigned']
      self.txt_model.text = vehicle_record[0]['model']
      self.txt_register_name.text = vehicle_record[0]['register_name']
      self.txt_plateno.text = vehicle_record[0]['plate_no']
      self.txt_engineno.text = vehicle_record[0]['engine_no']
      self.txt_chasisno.text = vehicle_record[0]['chasis_no']
      self.txt_status.text = vehicle_record[0]['status']  
      
      self.txt_crno.text = registration_record[0]['cr_no']
      self.txt_fdatecr.text = registration_record[0]['date_cr']
      self.txt_orno.text = registration_record[0]['or_no']
      self.txt_daterenew.text = registration_record[0]['date_renewed_or']
      self.txt_nextrenew.text = registration_record[0]['next_renewal']
    else:
      None

  

  def expand_button_click(self, **event_args):
    self.toggle_expand()

