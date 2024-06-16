from ._anvil_designer import MainTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from  .RegisterVehicle import RegisterVehicle
from .VehicleList import VehicleList
from .TransferVehicle import TransferVehicle


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()

    # Any code you write here will run before the form opens.

  def btn_register_click(self, **event_args):
   # self.card_1.clear()
    #self.card_1.add_component(RegisterVehicle())
    open_form('Main.RegisterVehicle')

  def btn_vehicleList_click(self, **event_args):
    #self.card_1.clear()
    #self.card_1.add_component(VehicleList())
    open_form('Main.VehicleList')

  def btn_transfer_click(self, **event_args):
    #self.card_1.clear()
    #self.card_1.add_component(TransferVehicle())
    open_form('Main.TransferVehicle')

  def btn_repair_approval_click(self, **event_args):
    open_form('Main.RepairApproval')
