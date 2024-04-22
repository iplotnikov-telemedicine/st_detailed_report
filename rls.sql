select 
    organisation_id
from reporting_job_position_view sm
where sm.job_position_status in ('ACTIVE', 'IMPORTED', 'INVITED')
    and job_position_id = '{job_position_id}'
limit 1