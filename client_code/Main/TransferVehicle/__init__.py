from ._anvil_designer import TransferVehicleTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TransferVehicle(TransferVehicleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_dropdown()

    # Any code you write here will run before the form opens.
  def refresh_dropdown(self):
    area_name = anvil.server.call('get_area')
    self.dp_area.items = area_name

  def button_2_click(self, **event_args):
    open_form('Main')

  def txt_plateno_pressed_enter(self, **event_args):
    search_plateno = self.txt_plateno.text
    vehicle_record = app_tables.vehicles.search(plate_no=search_plateno)
    
    if vehicle_record:
      self.txt_make.text = vehicle_record[0]['make']
      self.txt_color.text = vehicle_record[0]['color']
      self.txt_model.text = vehicle_record[0]['model']
      self.txt_bodytype.text = vehicle_record[0]['body_type']
      self.txt_registerName.text = vehicle_record[0]['register_name']
      self.txt_engineno.text = vehicle_record[0]['engine_no']
      self.txt_chassisno.text = vehicle_record[0]['chasis_no']  
    else:
      self.txt_make.text = ""

  def btn_transfer_click(self, **event_args):
    search_plateno = self.txt_plateno.text
    reason = self.txt_reason.text
    status = "Transfered"
    area = self.dp_area.selected_value
    date = self.dp_date.date
    record_history = anvil.server.call('record_vechicle_history', search_plateno, reason, status, area, date)
    update_area = anvil.server.call('update_trans_veh_status', search_plateno, area)
    if record_history and update_area:
      alert(f'Vechicle {search_plateno} has been tranfer')
    else:
      alert('Transfer failed!')
    
    
