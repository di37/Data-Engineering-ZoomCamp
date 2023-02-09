## Setting up GCP

- Download and install Google Cloud [SDK](https://cloud.google.com/sdk/docs/).
- Ensure all the components are up to date and also it should be done on regular basis:

```bash
gcloud components update
```

- Set environment variable to point to your downloaded GCP keys:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/isham993/Desktop/Programming-Tutorials/2022-Data-Engineering/Week_1/dtc-de-376913-bd4a59123085.json"

# Refresh token/session, and verify authentication
gcloud auth application-default login
```

It will re-direct to the browser for authentication.

## Setting up Terraform

- Now we will install [terraform](https://developer.hashicorp.com/terraform/downloads?product_intent=terraform).
- Create a new folder and other new files and copy the contents to the created files from original [repository](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp).

```bash
mkdir 1_terraform_gcp/terraform
cd 1_terraform_gcp
```

```
touch terraform/.terraform-version terraform/main.tf terraform/variables.tf
```

- Execution steps.
  - `terraform init`: Initialize and Install the Terraform environment.
  - `terraform plan`: Match changes against the previous state. Enter your GCP Project ID.
  - `terraform apply`: Apply changes to the cloud. Enter your GCP Project ID.

Lets go back to our project data and check whether bucket and bigquery dataset is created or not.

- To avoid unnecessary incurring of costs, we will delete the bucket and bigquery dataset: `terraform destroy`.
