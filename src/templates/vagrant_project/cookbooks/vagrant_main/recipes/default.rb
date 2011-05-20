require_recipe "apt"
require_recipe "apache2::mod_wsgi"
require_recipe "python"
require_recipe "mysql::server"
require_recipe "git"

execute "disable-default-site" do
  command "sudo a2dissite default"
  notifies :restart, resources(:service => "apache2")
end
