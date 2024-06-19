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

  def toggle_expand(self, **event_args):
    if not self.expanded:
      self.expanded_panel_details.visible = True
      self.expanded = True
    else:
      self.expanded_panel_details.visible = False
      self.expanded = False

    # Any code you write here will run before the form opens.

  def btn_home_click(self, **event_args):
    open_form('Main')

  def btn_view_click(self, **event_args):
    self.toggle_expand()
    results = app_tables.repairapproval.search(plate_no=self.txt_searchplateno.text)
    if results:
      self.txt_platenno.text = results[0]['plate_no']
      self.txt_area.text = results[0]['area']
      self.txt_name.text = results[0]['name']
      self.txt_date.text = results[0]['date']
      self.txt_desc.text = results[0]['description']
    else:
      alert('Theres no details on this plate no')
    
