variable "kubeconfig_path" {
  description = "Path to kubeconfig file"
  type = string
  default = "~/.kube/config"
}

variable "kubeconfig_context" {
  description = "Cluster context"
  type = string
  default = "test-k8s-cluster"
}

variable "service_name" {
  description = "kubernetes service name"
  type = string
  default = "python-test-web-app"
}

variable "namespace" {
  description = "namespace of the kubernetes service"
  type = string
  default = "test"
}