#!/usr/bin/env ruby
Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = 'http://files.vagrantup.com/precise64.box'

  inventory_files = File.expand_path("./ansible/inventory/files/", File.dirname(__FILE__))

  config.vm.provider :virtualbox do |virtualbox|
    virtualbox.customize ["modifyvm", :id, "--memory", 512]
  end

  config.vm.define :default do |node|
    node.vm.box = "precise64"
    node.vm.hostname = "vagrant"
    node.vm.network :forwarded_port, guest: 80, host: 8080
    node.vm.network :forwarded_port, guest: 8000, host: 8000
    
    node.vm.provision :ansible do |ansible|
      ansible.playbook = File.expand_path("./ansible/playbook/main.yml")
      ansible.sudo = true
      ansible.inventory_path = "./ansible/inventory/vagrant"
      ansible.extra_vars = { inventory_files: inventory_files }
      ansible.limit = 'all'
      ansible.verbose = 'v'
    end
  end

end
