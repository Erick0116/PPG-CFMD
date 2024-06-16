import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def register_vehicle(make, body_type, color, model, register_name, plate_no, engine_no, chasis_no, area_assigned, status, remarks):
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
def request_repair(plate_no, name, area, date, descrription):
  send_request = app_tables.repairapproval.add_row(
    plate_no=plate_no,
    name=name,
    area=area,
    date=date,
    description=descrription,
    status="Submitted"
  )
  if send_request:
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



  
