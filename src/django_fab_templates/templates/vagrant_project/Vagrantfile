Vagrant::Config.run do |config|
  config.vm.box = "lucid32"

  # Enable and configure the chef solo provisioner
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"
    chef.json.merge!({
      :mysql => {
        :server_root_password => "root"
      }
    })
    
    chef.add_recipe("vagrant_main")
  end
  
  # forward ports
  config.vm.forward_port("web", 80, 8080)
  config.vm.forward_port("mysql", 3306, 8806)
end
