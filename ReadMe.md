# Run in apache

install vagrant

    vagrant up

see http://localhost

# Run in dev server

    vagrant up
    vagrant ssh
    python /vagrant/FlaskApp.py

see http://localhost:5000

# My git config file

place it in $HOME/.gitconfig

    [user]
		email = blighli@gmail.com
		name = blighli
	[push]
		default = simple
	[credential]
		helper = store