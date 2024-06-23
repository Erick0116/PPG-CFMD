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
    self.refresh_dropdown()
    self.btn_submit.enabled = False
    self.check_user()

  def check_user(self):
    userlogin = anvil.users.get_user()
    if userlogin:
     # self.txt_user.text = userlogin['email']  # Display user's email (or username, if applicable)
      area = userlogin['area']
      self.dp_plateno.items = anvil.server.call('get_plateno', area)
    else:
      self.txt_user.text = "Not logged in"  # Handle case where no user is logged in
    

  def refresh_dropdown(self):
    area_name = anvil.server.call('get_area')
    self.dp_area.items = area_name

  def check_field(self):
    empty_fields = []
    if not self.dp_area.selected_value:
      empty_fields.append("Area")
    if not self.dp_plateno.selected_value:
      empty_fields.append("Plate Number")
    if not self.dp_date.date:
      empty_fields.append("Date")
    if not self.txt_mileage.text:
      empty_fields.append("Mileage")
    if not self.txt_explanation.text:
      empty_fields.append("Explanation")
    if not self.txt_shopname.text:
      empty_fields.append("Shop Name")
    if not self.txt_address.text:
      empty_fields.append("Address")
    if not self.txt_contactP.text:
      empty_fields.append("Contact Person")
    if not self.txt_contactNo.text:
      empty_fields.append("Contact Number")
    if not self.dp_due.date:
      empty_fields.append("Due Date")
    if not self.txt_scope.text:
      empty_fields.append("Scope")
    if not self.txt_amountlabor.text:
      empty_fields.append("Labor Amount")
    if not self.rp_parts.items:
      empty_fields.append("Part Items")
    if empty_fields:
        alert(f"The following fields are empty: {', '.join(empty_fields)}")
    else:
        self.validate_details()

  def validate_details(self):
    plate_no = self.dp_plateno.selected_value
    vehicle_record = app_tables.vehicles.search(plate_no=plate_no)
    try:
      if vehicle_record is not None:
        self.txt_make.text = vehicle_record[0]['make']
        self.txt_type.text = vehicle_record[0]['body_type']
        self.txt_model.text = vehicle_record[0]['model']
        
      else:
        alert(f'Plate no {plate_no} not found!')
    except IndexError:
      alert(f'Plate no {plate_no} not found!')
      
    

    # Any code you write here will run before the form opens.

  def btn_submit_click(self, **event_args):
    requesting_area = self.dp_area.selected_value
    make = self.txt_make.text
    type = self.txt_type.text
    model = self.txt_model.text
    date = self.dp_date.date
    plate_no = self.dp_plateno.selected_value
    mileage = int(self.txt_mileage.text)
    explanation = self.txt_explanation.text
    shop_name = self.txt_shopname.text
    address = self.txt_address.text
    contact_person = self.txt_contactP.text
    contact_no = self.txt_contactNo.text
    due_date = self.dp_date.date
    scope = self.txt_scope.text
    labor_amount = int(self.txt_amountlabor.text)
    total_parts = int(self.txt_amountParts.text)
    overall_total = int(self.txt_overalltotal.text)
    
    send_request = anvil.server.call('request_repair', requesting_area, make, type, model, date, plate_no, mileage, explanation, shop_name, address, contact_person, contact_no, due_date, scope, labor_amount, total_parts, overall_total)
    if send_request:
      alert(f"Your request for {plate_no} has been successfully submitted. Please wait for approval from the approver. You can check the request status for updates on approval.")
    else:
      alert("The submission of your request failed. Please try again")

  def btn_validation_click(self, **event_args):
    try:
      total_parts_amount = sum(item['amount'] for item in self.rp_parts.items)
      total_labor_amount = int(self.txt_amountlabor.text)
      self.txt_amountParts.text = total_parts_amount
      self.txt_overalltotal.text = total_labor_amount + total_parts_amount
      self.check_field()
      self.btn_submit.enabled = True
    except ValueError:
      alert('Lambor Amount is empty')
    
  def btn_add_items_click(self, **event_args):
    next_id_no = anvil.server.call('get_next_id')
    item = self.txt_item.text
    amount = int(self.txt_amount.text)
    date = self.dp_date.date
    plate_no = self.dp_plateno.selected_value
    parts_item = anvil.server.call('add_parts_item', next_id_no, plate_no, item, amount, date)
    if parts_item:
      self.rp_parts.items = anvil.server.call('parts_item_populate', plate_no, date)
    else:
      alert('Failed to add Please check the Plate No and Date is empty!')

  def txt_amountParts_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def dp_plateno_change(self, **event_args):
    self.validate_details()
      
    
    
    
    
