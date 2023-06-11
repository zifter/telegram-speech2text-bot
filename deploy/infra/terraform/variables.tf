variable "gcp_sa_credentials" {
  type        = string
  description = "Service Account key file"
}

variable "github_owner" {
  type        = string
  description = "Github Owner"
}

variable "github_token" {
  type        = string
  description = "Github Access Token"
}

variable "github_repository" {
  type        = string
  description = "Github Repository"
}

variable "gcp_project_name" {
  type        = string
  description = "GCP Project Name"
}

variable "gcp_region" {
  default = "europe-central2"
}

variable "gcp_zone" {
  default = "europe-central2-c"
}
