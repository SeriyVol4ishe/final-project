select
    cr.year as year,
    extract(month from cr.date) as month,
    coalesce(ca.community_name, 'undefined') as community_name,
    cr.location as location,
    cr.iucr as iucr,
    coalesce(iucr.is_active, false) as is_active,
    cr.primary_type as primary_type,
    cr.description as description,
    count(cr.id) as crimes_count
from {{ ref('stg_crime') }} as cr
left join {{ ref('stg_iucr') }} as iucr
    on cr.iucr = iucr.iucr
left join {{ ref('stg_community_area') }} as ca
    on cr.community_area = ca.area_num
group by
    year,
    community_name,
    month,
    location,
    iucr,
    is_active,
    primary_type,
    description
order by crimes_count desc
