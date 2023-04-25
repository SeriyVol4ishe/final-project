select
    model.iucr as id,
    model.iucr,
    model.primary_description,
    model.secondary_description,
    model.active
-- Alias added due to "bug": https://github.com/dbt-labs/dbt-bigquery/issues/33
from {{ source('staging', 'iucr') }} as model
