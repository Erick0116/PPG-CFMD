from ._anvil_designer import AreaRequestRepairTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AreaRequestRepair(AreaRequestRepairTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_repairs.items  = anvil.server.call('repair_populate')

    # Any code you write here will run before the form opens.

  def btn_submit_click(self, **event_args):
    plate_no = self.txt_plateno.text
    name = self.txt_name.text
    area = self.dp_area.selected_value
    date = self.dp_date.date
    desc = self.txt_desc.text
    send_request = anvil.server.call('request_repair', plate_no, name, area, date, desc)
    if send_request:
      alert(f"Your request for {plate_no} has been successfully submitted. Please wait for approval from the approver. You can check the request status for updates on approval.")
    else:
      alert("The submission of your request failed. Please try again")
    
    
