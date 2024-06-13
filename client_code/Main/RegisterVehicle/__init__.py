from ._anvil_designer import RegisterVehicleTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import get_dom_node


class RegisterVehicle(RegisterVehicleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

 

    # Any code you write here will run before the form opens.

  def btn_save_click(self, **event_args):
    make = self.txt_make.text
    body_type = self.txt_bodyType.text
    color = self.txt_color.text
    model  = self.txt_model.text
    register_name = self.txt_registerName.text
    plate_no = self.txt_plateno.text
    engine_no = self.txt_engineno.text
    chasis_no = self.txt_chasisno.text
    area_assigned = self.dp_area.selected_value
    status = self.dp_status.selected_value
    remarks = self.txt_remarks.text
    
    anvil.server.call('register_vehicle', make, body_type, color, model, register_name, plate_no, engine_no, chasis_no, area_assigned, status, remarks)
    alert("Vehicle has been added successfully!")

 


