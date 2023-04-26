# Final project

Final project for `Data Engineering Zoomcamp` course from [DataTalksClub](https://github.com/DataTalksClub)

## Table of contents

- [About project](#about-this-project)
    - [Motivation](#motivation)
    - [About data source](#about-data-source)
        - [Main dataset](#about-crimes---2001-to-present)
        - [Additional datasets](#about-additional-datasets)
    - [Project structure](#project-structure)
        - [Prerequisites](docs/PREREQUISITES.md)
        - [Terraform project documentation](terraform/README.md)
        - [AirFlow project documentation](airflow/README.md)
        - [DBT project documentation](dbt/README.md)
        - [Dashboards documentation](dashboards/README.md)
    - [Technology stack](#technology-stack)

## About this project

### Motivation

This project represents data pipeline in which data is extracted from source, transformed and loaded first
into `Google Cloud Storage` and then from `GCS` to `Google BigQuery` warehouse.

- Using this data we can:
    - To analyse crimes history and for specific community area
    - To analyse crimes history for specific crime type
    - To analyse crimes history for specific location
    - To assess the increase/decrease in the level of crime

### About data source

#### About [Crimes - 2001 to Present](https://data.cityofchicago.org/d/ijzp-q8t2)

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim)
that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from
the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system.

In order to protect the privacy of crime victims, addresses are shown at the block level only and
specific locations are not identified. Should you have questions about this dataset, you may contact
the Data Fulfillment and Analysis Division of the Chicago Police Department at DFA@ChicagoPolice.org.

**Disclaimer**:

These crimes may be based upon preliminary information supplied to the Police Department by the reporting parties
that have not been verified. The preliminary crime classifications may be changed at a later date
based upon additional investigation and there is always the possibility of mechanical or human error.
Therefore, the Chicago Police Department does not guarantee (either expressed or implied) the accuracy, completeness,
timeliness, or correct sequencing of the information and the information should not be used for comparison
purposes over time.

The Chicago Police Department will not be responsible for any error or omission, or for the use of,
or the results obtained from the use of this information. All data visualizations on maps should be considered
approximate and attempts to derive specific addresses are strictly prohibited.

The Chicago Police Department is not responsible for the content of any off-site pages that are referenced by or
that reference this web page other than an official City of Chicago or Chicago Police Department web page.

The user specifically acknowledges that the Chicago Police Department is not responsible for any defamatory,
offensive, misleading, or illegal conduct of other users, links, or third parties and that the risk of injury from
the foregoing rests entirely with the user.

The unauthorized use of the words "Chicago Police Department," "Chicago Police," or any colorable imitation
of these words or the unauthorized use of the Chicago Police Department logo is unlawful. This web page
([Crimes - 2001 to Present](https://data.cityofchicago.org/d/ijzp-q8t2)) does not, in any way, authorize such use.

To access a list of Chicago Police Department - Illinois Uniform Crime Reporting (IUCR) codes, go
to [link](http://data.cityofchicago.org/d/c7ck-438e)

#### About additional datasets

To access information about community areas go to [link](https://data.cityofchicago.org/d/cauq-8yn6)

To access information about wards (City Council district) go to [link](https://data.cityofchicago.org/d/sp34-6z76)

To access information about police districts go to [link](https://data.cityofchicago.org/d/fthy-xz3r)

To access information about police beats (smallest police geographic area – each beat has a dedicated police beat car)
go to [link](https://data.cityofchicago.org/d/aerh-rz74)

- Each dataset has Socrata API documentation that can be accessed by link:
    - [crime](https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t2)
    - [iucr](https://dev.socrata.com/foundry/data.cityofchicago.org/c7ck-438e)
    - [community_area](https://dev.socrata.com/foundry/data.cityofchicago.org/igwz-8jzy)
    - [ward](https://dev.socrata.com/foundry/data.cityofchicago.org/k9yb-bpqx)
    - [district](https://dev.socrata.com/foundry/data.cityofchicago.org/24zt-jpfn)
    - [beat](https://dev.socrata.com/foundry/data.cityofchicago.org/n9it-hstw)

### Project structure

```
airflow /      contains Airflow project for data orchestration
credentials /  contains json keys for GCP service account (empty for obvious reasons)
dashboards  /  contains dashboards created with Google Looker Studio
dbt /          contains DBT project for data transformation
docs /         contains files and images for project documentation
terraform /    contains Terraform project for initialization of project infrastructure in GCP
```

### Technology stack

- Google Cloud Platform
    - Google Cloud Storage
    - BigQuery
- Terraform
- Airflow
- DBT
- Docker
