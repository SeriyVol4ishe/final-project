select
    cr.year as year,
    coalesce(ca.community_name, 'undefined') as community_name,
    count(cr.id) as crimes_count
from {{ ref('stg_crime') }} as cr
left join {{ ref('stg_community_area') }} as ca
    on cr.community_area = ca.area_num
group by cr.year, ca.community_name order by crimes_count desc
