from ._anvil_designer import RepairApprovalTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RepairApproval(RepairApprovalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_repair.items  = anvil.server.call('repair_populate')
    self.expanded  = False
    self.exapand_panel.visible = False

  def toggle_expand(self, **event_args):
    if not self.expanded:
      self.exapand_panel.visible = True
      self.expanded = True
    else:
      self.exapand_panel.visible = False
      self.expanded = False
    

    # Any code you write here will run before the form opens.

    

  def btn_disapprove_click(self, **event_args):
    #self.toggle_expand()
    self.toggle_expand()  

  def btn_approve_click(self, **event_args):
    plate_no = self.txt_plateno.text
    record = anvil.server.call('update_repair_status', plate_no)
    if record:
      alert(f'{plate_no} repair request has been approve succesfully!')
      self.rp_repair.items  = anvil.server.call('repair_populate')
    else:
      alert('Approval Failed!')

  def btn_save_click(self, **event_args):
    plate_no = self.txt_plateno.text
    remarks = self.txt_remarks.text
    record = anvil.server.call('disapprove_repair', plate_no, remarks)
    if record:
      alert(f'{plate_no} repair has been disapprove sucessfully!')
      self.rp_repair.items  = anvil.server.call('repair_populate')
    else:
      alert('Disapproval Failed!')

  def btn_home_click(self, **event_args):
    open_form('Main')

  def btn_search_click(self, **event_args):
    search_plateno =  self.txt_search.text
    repair_details = app_tables.repairapproval.search(plate_no=search_plateno)
    try:
      if repair_details:
        self.txt_area.text = repair_details[0]['requesting_area']
        self.txt_plateno.text = repair_details[0]['plate_no']
        self.txt_date.text = repair_details[0]['date']
        self.txt_make.text = repair_details[0]['make']
        self.txt_type.text = repair_details[0]['type']
        self.txt_model.text = repair_details[0]['model']
        self.txt_explanation.text = repair_details[0]['explanation']
        self.txt_shopname.text = repair_details[0]['shop_name']
        self.txt_address.text = repair_details[0]['address']
        self.txt_contactP.text = repair_details[0]['contact_person']
        self.txt_contactNo.text = repair_details[0]['contact_no']
        self.txt_due.text = repair_details[0]['due_date']
        self.txt_scope.text = repair_details[0]['scope']
        self.txt_amountlabor.text = repair_details[0]['labor_amount']
        self.txt_amountParts.text = repair_details[0]['total_parts']
        self.txt_overalltotal.text = repair_details[0]['overall_total']
      else:
        alert('Plate number not found')
    except IndexError:
      alert('Please check for any leading or trailing spaces in the Plate No text field.')
    
