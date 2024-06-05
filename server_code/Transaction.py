import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def  register_vehicle(make, body_type, color, model, register_name, plate_no, engine_no, chasis_no, area_assigned, status, remarks, cr_no, date_cr, or_no, date_renewed_or, next_renewal, insurance_type, insurance_name, premium, coverage, expiry):
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
    remarks=remarks,
    cr_no=cr_no,
    date_cr=date_cr,
    or_no=or_no,
    date_renewed_or=date_renewed_or,
    next_renewal=next_renewal,
    insurance_type=insurance_type,
    insurance_name=insurance_name,
    premium=premium,
    coverage=coverage,
    expiry=expiry
  )
  
