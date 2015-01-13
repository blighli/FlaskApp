Vagrant.configure(2) do |config|
    
    config.vm.box = "ubuntu/trusty64"

	config.vm.network "forwarded_port", guest: 80, host: 80
	config.vm.network "forwarded_port", guest: 5000, host: 5000

	config.vm.provision "shell", inline: <<-SHELL
		sudo apt-get update
		sudo apt-get install -y apache2
		sudo apt-get install -y libapache2-mod-wsgi
		sudo apt-get install -y python-pip
		sudo pip install flask
	
		sudo ln -s /vagrant /var/www/vagrant
		sudo ln -s /vagrant/flask-site.conf /etc/apache2/sites-enabled/flask-site.conf
		sudo service apache2 restart
	SHELL
end