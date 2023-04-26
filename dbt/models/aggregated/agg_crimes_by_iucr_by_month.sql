select
    cr.year as year,
    coalesce(ca.community_name, 'undefined') as community_name,
    extract(month from cr.date) as month,
    cr.iucr,
    iucr.is_active,
    iucr.primary_type,
    iucr.description,
    count(cr.id) as crimes_count
from {{ ref('stg_crime') }} as cr
left join {{ ref('stg_iucr') }} as iucr
    on cr.iucr = iucr.iucr
left join {{ ref('stg_community_area') }} as ca
    on cr.community_area = ca.area_num
where ca.area_num is not null
group by
    year,
    community_name,
    month,
    iucr,
    is_active,
    primary_type,
    description
order by crimes_count desc
