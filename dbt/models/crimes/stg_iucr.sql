select
    model.iucr as id,
    right('000'||model.iucr, 4) as iucr,
    model.primary_description as primary_type,
    model.secondary_description as description,
    model.active as is_active
-- Alias added due to "bug": https://github.com/dbt-labs/dbt-bigquery/issues/33
from {{ source('staging', 'iucr') }} as model
