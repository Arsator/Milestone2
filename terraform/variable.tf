variable "aws_region" {
  description = "AWS Region"
  default     = "ap-south-1"
}

variable "app_image" {
  description = "Name of Image"
  default     = "public.ecr.aws/t2u6r1h4/my-app"
}

variable "az_count" {
  description = "Number of availability zones"
  default     = "2"
}
variable "app_port" {
  default = 5000
}
variable "health_check_path" {
  default = "/"
}

variable "fargate_cpu" {
    default = "256"
}

variable "fargate_memory" {
    default = "512"
}