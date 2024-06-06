from ._anvil_designer import VehicleListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class VehicleList(VehicleListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_vehicles.items  = anvil.server.call('vehicles_populate')

    # Any code you write here will run before the form opens.

  def btn_search_click(self, **event_args):
    self.rp_vehicles.items  = anvil.server.call('search_vehicles', self.txt_search.text)
