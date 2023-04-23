select
    id,
    case_number,
    date,
    block,
    iucr,
    primary_type,
    description,
    location_description,
    arrest,
    domestic,
    beat,
    district,
    ward,
    community_area,
    fbi_code,
    year,
    updated_on,
    latitude,
    longitude,
from {{ source('staging', 'crime') }}