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
    user = anvil.users.get_user()
    if user is not None:
      if user['role'] == 'area':
        self.btn_register.visible = False
        self.btn_transfer.visible = False
        self.btn_vehicleList.visible = False
        self.btn_repair_approval.visible  = False
        self.card_count_approval.visible = False
        self.card_total_vehicle.visible = False
        self.card_total_sold.visible = False
        self.card_2.visible = False
        self.btn_acount.visible = False
        self.btn_request_repair.visible = True
        self.btn_viewRequest.visible = True
      elif user['role'] == 'admin':
        self.btn_request_repair.visible = False
        self.btn_viewRequest.visible = False
      else:
        alert('You dont have the prreviledge to access the page')
    self.check_user()    
    self.total_repair_approval()
    self.total_vehicle()

  def check_user(self):
    userlogin = anvil.users.get_user()
    if userlogin:
     # self.txt_user.text = userlogin['email']  # Display user's email (or username, if applicable)
      self.user_login.text = userlogin['email']
    else:
      self.txt_user.text = "Not logged in"  # Handle case where no user is logged in
    
  def total_repair_approval(self, **event_args):
    results = app_tables.repairapproval.search(status="Requested")
    count = 0
    for record in results:
        count += 1  # Increment count for each record found    
    self.lbl_count.text= str(count)  # Convert count to string for assignment

  def total_vehicle(self, **event_args):
    results = app_tables.vehicles.search(status="Active")
    count = 0
    for record in results:
      count += 1
    self.lbl_count_vehicle.text = str(count)

      
      
    

  
  
   
      
     

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

  def btn_viewRequest_click(self, **event_args):
    open_form('Main.ViewRequest')

  def btn_request_repair_click(self, **event_args):
    open_form('Main.AreaRequestRepair')

  def btn_view_repair_click(self, **event_args):
    open_form('Main.RepairApproval')

  def login_click(self, **event_args):
    anvil.users.logout()
    open_form('Main')

  def btn_acount_click(self, **event_args):
    open_form('Main.UserAccount')
