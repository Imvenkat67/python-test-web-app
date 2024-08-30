data "kubernetes_service" "python_test_web_app" {
  metadata {
    name = var.service_name
    namespace = var.namespace
  }
}

resource "local_file" "service_details" {
  filename = "k8s_service_details.json"
  content = jsonencode({
    name       = data.kubernetes_service.python_test_web_app.metadata[0].name
    namespace  = data.kubernetes_service.python_test_web_app.metadata[0].namespace
    cluster_ip = data.kubernetes_service.python_test_web_app.spec[0].cluster_ip
    port       = data.kubernetes_service.python_test_web_app.spec[0].port[0].port
  })
}