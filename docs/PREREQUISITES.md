## Apps to install:

> `docker`
>
> `docker-compose`
>
> `terraform`

## Google Cloud Project

1. In the Google Cloud console, go to [Create a Project](https://console.cloud.google.com/projectcreate)

2. In the Project Name field, enter a descriptive name for your project.

   **Optional:** To edit the Project ID, click Edit. The project ID can't be changed after the project is created, so
   choose an ID that meets your needs for the lifetime of the project.

   ![img.png](../docs/poc/gcp/gcp_project_creation.png)

3. Click Create. The console navigates to the Dashboard page and your project is created within a few minutes.

   ![img.png](../docs/poc/gcp/gcp_project_dashboard.png)

4. After creation a project you have to create service account. Go
   to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) and choose your project:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_page.png)

5. Click on `CREATE SERVICE ACCOUNT`, enter the name and (optional) account ID and description and
   click `CREATE AND CONTINUE`:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_create_account.png)

6. Grant this service account access to project's `BigQuery` and `GCS` resources and data and click `CONTINUE`:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_grant_access.png)

7. Click `DONE`:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_final_step.png)

8. Click on `Email` value of created account:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_click_email.png)

9. Go to `KEYS` section of the opened page and create new key:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_keys_section.png)

   ![img.png](../docs/poc/gcp/gcp_service_accounts_click_create_new_key.png)

   ![img.png](../docs/poc/gcp/gcp_service_accounts_click_create_new_key_json.png)

10. After click on `CREATE` button the private key will be saved on your computer:

   ![img.png](../docs/poc/gcp/gcp_service_accounts_click_create_new_key_json_downloaded.png)

11. Now you have to copy this JSON file to the `credentials` folder of your cloned project and rename this file
    to `credentials.json`:

   ![img.png](../docs/poc/gcp/gcp_credentials_json.png)

## App Token Creation

1. Register on [Chicago Data Portal](https://data.cityofchicago.org/signup)

2. Sign in:

   ![img.png](../docs/poc/cityofchicago/cityofchicago_home.png)

3. Go to [Profile Edit | Developer Settings](https://data.cityofchicago.org/profile/edit/developer_settings) page:

   ![img.png](../docs/poc/cityofchicago/cityofchicago_developer_settings.png)

4. Create new `App Token`:

   ![img.png](../docs/poc/cityofchicago/cityofchicago_app_token_creation.png)
   ![img.png](../docs/poc/cityofchicago/cityofchicago_app_token.png)

5. Copy created `App Token` and put this value in file `airflow/variables_and_connections/variables.json` as a value
   for the `app_token` key:

   ![img.png](../docs/poc/cityofchicago/variables_json_app_token.png)

## Set GCS Bucket Variable

1. Create infrastructure with `terraform` following this [instructions](/terraform/README.md#local-setup-and-run).
2. See logs and find the name of bucket created by `terraform`:

   ![img.png](../docs/poc/terraform/log_with_bucket_name.png)

3. Copy the name of created bucket and put this value in file `airflow/variables_and_connections/variables.json` as a
   value
   for keys `destination_bucket` and `source_bucket`:

   ![img.png](../docs/poc/cityofchicago/variables_json_bucket_name.png)
