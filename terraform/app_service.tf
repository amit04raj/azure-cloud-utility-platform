resource "azurerm_service_plan" "utility_hub" {
  name                = "asp-utility-hub"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location

  os_type  = "Linux"
  sku_name = "B1"

  tags = {
    project     = "utility-hub"
    environment = "portfolio"
    managed_by  = "terraform"
  }
}

resource "azurerm_linux_web_app" "utility_hub" {
  name                = "app-utility-hub"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_service_plan.utility_hub.location
  service_plan_id     = azurerm_service_plan.utility_hub.id

  https_only                                     = true
  ftp_publish_basic_authentication_enabled       = false
  webdeploy_publish_basic_authentication_enabled = false

  app_settings = {
    SCM_DO_BUILD_DURING_DEPLOYMENT = "true"
  }

  site_config {
    minimum_tls_version = "1.2"

    app_command_line = "python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"

    application_stack {
      python_version = "3.12"
    }
  }

  tags = {
    project     = "utility-hub"
    environment = "portfolio"
    managed_by  = "terraform"
  }
}