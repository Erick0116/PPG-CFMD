from ._anvil_designer import UserAccountTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class UserAccount(UserAccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rp_users.items = anvil.server.call('user_account')
    self.refresh_dropdown()

    # Any code you write here will run before the form opens.
  def refresh_dropdown(self):
    area_name = anvil.server.call('get_area')
    self.dp_area.items = area_name

  def btn_search_click(self, **event_args):
    email = self.txt_email.text
    self.rp_users.items = app_tables.users.search(email=email)

  def btn_update_click(self, **event_args):
    email = self.txt_email.text
    role = self.dp_role.selected_value
    area = self.dp_area.selected_value
    users = anvil.server.call('update_user', email, role, area)
    if users:
      alert(f'User {self.txt_email.text} has been updated succesfully!')
    else:
      alert('User failed to update!')

  def btn_cancel_click(self, **event_args):
    open_form('Main')