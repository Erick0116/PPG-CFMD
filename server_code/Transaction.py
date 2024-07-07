import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def register_vehicle(make, body_type, color, model, register_name, plate_no, engine_no, chasis_no, area_assigned, ownership, status, remarks):
  app_tables.vehicles.add_row(
    make=make,
    body_type=body_type,
    color=color,
    model=model,
    register_name=register_name,
    plate_no=plate_no,
    engine_no=engine_no,
    chasis_no=chasis_no,
    area_assigned=area_assigned,
    ownership=ownership,
    status=status,
    remarks=remarks
  )

@anvil.server.callable
def add_registration(plate_no, cr_no, date_cr, or_no, date_renewed_or, next_renewal):
  app_tables.registration.add_row(
    plate_no=plate_no,
    cr_no=cr_no,
    date_cr=date_cr,
    or_no=or_no,
    date_renewed_or=date_renewed_or,
    next_renewal=next_renewal
  )

@anvil.server.callable
def add_insurance(plate_no, insurance_type, insurance_name, premium, coverage, expiry):
  app_tables.insurance.add_row(
    plate_no=plate_no,
    insurance_type=insurance_type,
    insurance_name=insurance_name,
    premium=premium,
    coverage=coverage,
    expiry=expiry
  )

@anvil.server.callable
def request_repair(requesting_area, make, type, model, date, plate_no, mileage, explanation, shop_name, address, contact_person, contact_no, due_date, scope, labor_amount, total_parts, overall_total, request_no):
  send_request = app_tables.repairapproval.add_row(
    requesting_area=requesting_area,
    make=make,
    type=type,
    model=model,
    date=date,
    plate_no=plate_no,
    mileage=mileage,
    explanation=explanation,
    shop_name=shop_name,
    address=address,
    contact_person=contact_person,
    contact_no=contact_no,
    due_date=due_date,
    scope=scope,
    labor_amount=labor_amount,
    total_parts=total_parts,
    overall_total=overall_total,
    status="Requested",
    request_no=request_no
  )
  if send_request:
    return True
  else: 
    return False

@anvil.server.callable
def add_parts_item(id, plate_no, item, amount, date):
  part_items = app_tables.partsitem.add_row(
    id=id,
    plate_no=plate_no,
    item=item,
    amount=amount,
    date=date,
    status='Requested'
  )
  if part_items:
    return True
  else:
    return False
  

@anvil.server.callable
def record_vechicle_history(plate_no, reason, status, area, date):
  app_tables.transferhistory.add_row(
    plate_no=plate_no,
    reason=reason,
    status=status,
    area=area,
    date=date
  )
  return True

@anvil.server.callable
def update_trans_veh_status(plate_no, area):
  vehicle_record = app_tables.vehicles.get(plate_no=plate_no)
  if vehicle_record is not None:
    vehicle_record['area_assigned'] = area
    vehicle_record.update()
    return True
  else:
    return False

@anvil.server.callable
def update_repTicketStatus(request_no, ticket_status):
  record = app_tables.repairapproval.get(request_no=request_no)
  if record is not None:
    record['ticket_status'] = ticket_status
    record.update()
    return True
  else:
    return False

@anvil.server.callable
def update_repairRemarks(request_no, remarks):
  record = app_tables.repairapproval.get(request_no=request_no)
  if record is not None:
    record['remarks'] = remarks
    record.update()
    return True
  else:
    return False
    
@anvil.server.callable
def update_user(email, role, area):
  users = app_tables.users.get(email=email)
  if users:
    users['role'] = role
    users['area'] = area
    users.update()
    return True
  else:
    return False

@anvil.server.callable
def update_repair_status(plate_no):
  record = app_tables.repairapproval.get(plate_no=plate_no)
  if record:
    record['status'] = "Approved"
    record.update()
    return True
  else:
    return False

@anvil.server.callable
def update_parts_status(plate_no):
  parts_item = app_tables.partsitem.get(plate_no=plate_no)
  if parts_item['status'] == 'Requested':
    parts_item['status'] = 'Approved'
    parts_item.update()
    return True
  else:
    return False
    
@anvil.server.callable
def disapprove_repair(plateno, remarks):
  record = app_tables.repairapproval.get(plate_no=plateno)
  if record is not None:
    record['status'] = "Disapproved"
    record['remarks'] = remarks
    record.update()
    return True
  else:
    return False

@anvil.server.callable
def get_area():
  area_name = [area['area_name']for area in app_tables.area.search()]
  return area_name

@anvil.server.callable
def get_plateno(area):
  plate_no = [plateno['plate_no']for plateno in app_tables.vehicles.search(area_assigned=area)]
  return plate_no



  
