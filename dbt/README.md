# DBT Docs
## Content:
- [Prerequisites](#prerequisites)
- [Local setup and run](#local-setup-and-run)
- [Setup in DBT Cloud](#setup-in-dbt-cloud)
- [Resources](#resources)

## Prerequisites:

1. Install dbt:
   `pip install dbt-bigquery`

## Local setup and run:

1. Change project value and path to your credentials json in `profiles.yml`
2. Run `cd dbt`:

   ![img.png](../docs/poc/dbt/cd_dbt.png)

3. Run `dbt build`:

   ![img.png](../docs/poc/dbt/dbt_build.png)

4. Run `dbt run`:

   ![img.png](../docs/poc/dbt/dbt_run.png)
   ![img.png](../docs/poc/gcp/bigquery_dbt_models.png)

5. To generate docs and see it in browser run `dbt docs generate`
   and then `dbt docs serve --port <port>` and open link `localhost:<port>`:

   ![img.png](../docs/poc/dbt/dbt_docs_generate.png)
   ![img.png](../docs/poc/dbt/dbt_docs_serve.png)
   ![img.png](../docs/poc/dbt/dbt_docs_browser.png)

## Setup in DBT Cloud:

1. Create account in [getdbt.com](https://www.getdbt.com/) or login if you have one.
2. After login create a new account:

![img.png](../docs/poc/dbt/cloud_create_account.png)

3. Choose a BigQuery connection:

![img.png](../docs/poc/dbt/cloud_choose_connection.png)

4. Configure environment by uploading Service Account JSON file:

![img.png](../docs/poc/dbt/cloud_json_file.png)

5. Choose dataset for models build and test connection:

![img.png](../docs/poc/dbt/cloud_choose_dataset.png)
![img.png](../docs/poc/dbt/cloud_test_connection.png)

6. Choose your repository on `Setup a Repository` step in dbt cloud:

![img.png](../docs/poc/dbt/cloud_setup_repository.png)

7. Project is ready:

![img.png](../docs/poc/dbt/cloud_enjoy.png)

8. Due to existence of dbt project inside a subdirectory you need to set `Project subdirectory` setting:

- Go to the `Account Settings`:

  ![img.png](../docs/poc/dbt/cloud_init_account_settings.png)

- Tap on your project name:

  ![img.png](../docs/poc/dbt/cloud_init_choose_project.png)

- Click `Edit` button and set `Project subdirectory` to `dbt`:

  ![img.png](../docs/poc/dbt/cloud_init_choose_subdirectory.png)

- Click on `Save` button:

  ![img.png](../docs/poc/dbt/cloud_init_subdirectory_saved.png)

9. Go to `Develop` section and create new branch:

   ![img.png](../docs/poc/dbt/cloud_create_branch.png)

10. Enjoy:

    ![img.png](../docs/poc/dbt/cloud_dbt_build.png)

### Resources:

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](http://community.getbdt.com/) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
