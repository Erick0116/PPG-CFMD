from ._anvil_designer import RowTemplate13Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate13(RowTemplate13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_row_panel_write_view.visible = False

    # Any code you write here will run before the form opens.

  def btn_edit_click(self, **event_args):
    self.data_row_panel_write_view.visible = True
    self.data_row_panel_read_view.visible = False

  def btn_close_click(self, **event_args):
    self.data_row_panel_write_view.visible = False
    self.data_row_panel_read_view.visible = True

  def btn_approve_click(self, **event_args):
    record = anvil.server.call('update_repTicketStatus', self.lbl_requestno.text, self.dp_status.selected_value)
    if record:
      alert(f"Record {self.lbl_plateno.text} status hass been updated  successfully!")
    else:
      alert("Update failed")
