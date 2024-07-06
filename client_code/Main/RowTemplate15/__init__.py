from ._anvil_designer import RowTemplate15Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate15(RowTemplate15Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_row_panel_write_view_pending.visible = False

    # Any code you write here will run before the form opens.

  def btn_edit_onhold_click(self, **event_args):
    self.data_row_panel_write_view_pending.visible = True
    self.data_row_panel_read_view_pending.visible = False
