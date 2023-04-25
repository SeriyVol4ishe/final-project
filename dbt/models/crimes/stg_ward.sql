select
    model.ward as id,
    model.ward,
    model.shape_leng,
    model.shape_area
-- Alias added due to "bug": https://github.com/dbt-labs/dbt-bigquery/issues/33
from {{ source('staging', 'ward') }} as model
