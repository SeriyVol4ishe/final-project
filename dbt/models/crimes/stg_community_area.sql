select
    area_num as id,
    area_num,
    community as community_name
from {{ source('staging', 'community_area') }}