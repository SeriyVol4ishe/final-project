select
    beat_num as id,
    beat,
    beat_num,
    district,
    sector
from {{ source('staging', 'beat') }} as model
