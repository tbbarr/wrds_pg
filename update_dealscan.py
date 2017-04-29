#!/usr/bin/env python3
from sqlalchemy import create_engine
import os
dbname = os.getenv("PGDATABASE")
host = os.getenv("PGHOST", "localhost")
wrds_id = os.getenv("WRDS_ID")
dbname = engine = create_engine("postgresql://" + host + "/" + dbname)

from wrds_fetch import wrds_update

wrds_update("borrowerbase", "dealscan", engine, wrds_id)
wrds_update("company", "dealscan", engine, wrds_id)
wrds_update("currfacpricing", "dealscan", engine, wrds_id)
wrds_update("dealamendment", "dealscan", engine, wrds_id)
wrds_update("dealpurposecomment", "dealscan", engine, wrds_id)
wrds_update("facility", "dealscan", engine, wrds_id)
wrds_update("facilityamendment", "dealscan", engine, wrds_id)
wrds_update("facilitydates", "dealscan", engine, wrds_id)
wrds_update("facilityguarantor", "dealscan", engine, wrds_id)
wrds_update("facilitypaymentschedule", "dealscan", engine, wrds_id)
wrds_update("facilitysecurity", "dealscan", engine, wrds_id)
wrds_update("facilitysponsor", "dealscan", engine, wrds_id)
wrds_update("financialcovenant", "dealscan", engine, wrds_id)
wrds_update("financialratios", "dealscan", engine, wrds_id)
wrds_update("lendershares", "dealscan", engine, wrds_id)
wrds_update("link_table", "dealscan", engine, wrds_id)
wrds_update("lins", "dealscan", engine, wrds_id)
wrds_update("marketsegment", "dealscan", engine, wrds_id)
wrds_update("networthcovenant", "dealscan", engine, wrds_id)
wrds_update("organizationtype", "dealscan", engine, wrds_id)
wrds_update("package", "dealscan", engine, wrds_id)
wrds_update("packageassignmentcomment", "dealscan", engine, wrds_id)
wrds_update("performancepricing", "dealscan", engine, wrds_id)
wrds_update("performancepricingcomments", "dealscan", engine, wrds_id)
wrds_update("sublimits", "dealscan", engine, wrds_id)
wrds_update("dbo_df_fac_dates_data", "dealscan", engine, wrds_id)
