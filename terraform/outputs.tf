output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "resource_group_location" {
  value = azurerm_resource_group.main.location
}

output "web_app_hostname" {
  value = azurerm_linux_web_app.utility_hub.default_hostname
}