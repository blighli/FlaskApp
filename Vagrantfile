Vagrant.configure(2) do |config|
    
    config.vm.box = "ubuntu/trusty64"

    config.vm.network "forwarded_port", guest: 80, host: 80

	#config.vm.provision "shell", inline: <<-SHELL
	#	sudo apt-get update
	#	sudo apt-get install -y apache2
	#	sudo apt-get install -y libapache2-mod-wsgi
	#	sudo apt-get install -y python-pip
	#	sudo 
	#SHELL
end