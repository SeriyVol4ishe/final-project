select
    dist_num as id,
    dist_num as district_number,
    dist_label as district_label
from {{ source('staging', 'district') }}