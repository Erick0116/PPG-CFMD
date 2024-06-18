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

    # Any code you write here will run before the form opens.
