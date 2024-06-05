from ._anvil_designer import RegisterVehicleTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


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
    cr_no = self.txt_crno.text
    date_cr = self.dp_datecr.date
    or_no = self.txt_orno.text
    date_renewal_or = self.dp_dateRenew.date
    next_renewal = self.dp_nextRenewed.date
    insurance_type =  self.txt_insuranceType.text
    insurance_name = self.txt_insuranceName.text
    premium = int(self.txt_premium.text)
    coverage = int(self.txt_coverage.text)
    expiry = self.dp_expiry.date
    anvil.server.call('register_vehicle', make, body_type, color, model, register_name, plate_no, engine_no, chasis_no, area_assigned, status, remarks, cr_no, date_cr, or_no, date_renewal_or, next_renewal, insurance_type, insurance_name, premium, coverage, expiry)
    alert("Vehicle has been added successfully!")
