# Logs Analysis
Udacity full stack web developer Logs Analysis project.

### Prerequisites
1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/)
3. [A terminal, such as Git Bash](https://git-scm.com/downloads)
4. [Udacity VM Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
5. [Project Starter Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### VM Installation
1. Install VirtualBox then Vagrant
2. Unzip the VM configuation and `cd` into the `vagrant` folder
3. Start the VM by typing the command `vagrant up` (it may take a few minutes to run)
4. When the VM is running type `vagrant ssh` in the terminal to log in

### Database Setup
1. Unzip the project starter data into the `vagrant` directory
2. Login to the VM and use the command `psql -d news -f newsdata.sql` to create and connect to the database
