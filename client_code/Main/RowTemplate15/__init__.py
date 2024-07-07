from ._anvil_designer import RowTemplate15Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class RowTemplate15(RowTemplate15Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_row_panel_write_view_pending.visible = False
    self.expanded = False
    self.expanded_panel_onhold.visible = False

  def toggle_expand(self, **event_args):
    if not self.expanded:
      self.expanded_panel_onhold.visible = True
      self.expanded = True
      
    else:
      self.expanded_panel_onhold.visible = False
      self.expanded = False

  

    # Any code you write here will run before the form opens.

  def btn_edit_onhold_click(self, **event_args):
    self.data_row_panel_write_view_pending.visible = True
    self.data_row_panel_read_view_pending.visible = False

  def btn_updateOnhold_click(self, **event_args):
    record = anvil.server.call('update_repTicketStatus', self.lbl_requestnoOnhold.text, self.dp_status_onhold.selected_value)
    if record is not None:
      alert(f"Record {self.lbl_requestnoOnhold.text} status hass been updated  successfully!")
      open_form('Main')
    else:
      alert("Status should not be empty")

  def dp_status_onhold_change(self, **event_args):
    self.btn_updateOnhold.enabled = False
    if self.dp_status_onhold.selected_value == "Approved":
      self.toggle_expand()

  def btn_save_onhold_click(self, **event_args):
    record = anvil.server.call('update_repairRemarks', self.txt_remarks_onhold.text, self.txt_remarks_onhold.text)
    update_status = anvil.server.call('update_repTicketStatus', self.dp_status_onhold.selected_value)
    if record and update_status:
      alert(f'Plate No {self.lbl_plateno.text} approval has been updated successfully!')
    else:
      alert('Update failed!!!')

  def btn_generate_approverNo_click(self, **event_args):
    plate_no = self.lbl_plateno_onhold.text
    next_id_no = anvil.server.call('get_next_id')
    current_time = datetime.now().strftime('%Y%m%d')
    request_no = f"{current_time}_{plate_no}_{next_id_no}"