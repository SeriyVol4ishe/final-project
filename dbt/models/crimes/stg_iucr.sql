select
    iucr as id,
    iucr,
    primary_description,
    secondary_description,
    active
from {{ source('staging', 'iucr') }}