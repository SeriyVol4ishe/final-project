select
    cr.year as year,
    cr.month as month,
    cr.primary_type,
    sum(cr.crimes_count) as crimes_count
from {{ ref('agg_crimes_by_iucr_by_month') }} as cr
group by
    year,
    month,
    primary_type
order by
    year,
    month
