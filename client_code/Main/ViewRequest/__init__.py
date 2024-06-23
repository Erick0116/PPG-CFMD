from ._anvil_designer import ViewRequestTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ViewRequest(ViewRequestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_repairs.items  = anvil.server.call('repair_populate')
    self.expanded = False
    self.expanded_panel_details.visible = False
    self.check_user()

  def toggle_expand(self, **event_args):
    if not self.expanded:
      self.expanded_panel_details.visible = True
      self.expanded = True
    else:
      self.expanded_panel_details.visible = False
      self.expanded = False

    # Any code you write here will run before the form opens.
  def check_user(self):
    userlogin = anvil.users.get_user()
    if userlogin:
     # self.txt_user.text = userlogin['email']  # Display user's email (or username, if applicable)
      area = userlogin['area']
      self.dp_plateno.items = anvil.server.call('get_plateno', area)
    else:
      self.txt_user.text = "Not logged in"  # Handle case where no user is logged in

  def btn_home_click(self, **event_args):
    open_form('Main')

  def btn_view_click(self, **event_args):
    self.toggle_expand()
    results = app_tables.repairapproval.search(plate_no=self.dp_plateno.selected_value)
    if results:
      self.txt_area.text = results[0]['requesting_area']
      self.txt_platenno.text = results[0]['plate_no']
      self.txt_date.text = results[0]['date']
      self.txt_mileage.text = results[0]['mileage']
      self.txt_make.text = results[0]['make']
      self.txt_type.text = results[0]['type']
      self.txt_model.text = results[0]['model']
      self.txt_explanation.text = results[0]['explanation']
      self.txt_shopname.text = results[0]['shop_name']
      self.txt_address.text = results[0]['address']
      self.txt_contactP.text = results[0]['contact_person']
      self.txt_contactNo.text = results[0]['contact_no']
      self.txt_due.text = results[0]['due_date']
      self.txt_scope.text = results[0]['scope']
      self.txt_amountlabor.text = results[0]['labor_amount']
      self.txt_amountParts.text = results[0]['total_parts']
      self.txt_overalltotal.text = results[0]['overall_total']
      self.rp_partsitem.items = app_tables.partsitem.search(plate_no=self.dp_plateno.selected_value)
    else:
      alert('Theres no details on this plate no')
    
