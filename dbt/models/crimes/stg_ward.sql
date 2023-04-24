select
    ward as id,
    ward,
    shape_leng,
    shape_area
from {{ source('staging', 'ward') }}