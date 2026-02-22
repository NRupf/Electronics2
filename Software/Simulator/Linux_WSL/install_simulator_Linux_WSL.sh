sudo apt -y update
sudo apt -y upgrade

# install the simulator and gtkwave
sudo apt -y install gtkwave
sudo apt -y install verilator
sudo apt -y install make
sudo apt -y install g++


# python environments
sudo apt -y install python3-venv
sudo apt -y install python3-pip


# clean up
sudo apt -y update
sudo apt -y upgrade
sudo apt -y autoremove

# Setup Python environment (as user):
python3 -m venv ~/efp
source ~/efp/bin/activate
python3 -m pip install --upgrade pip
pip install cocotb==1.9.2
pip install jupyter
pip install scipy

# To uninstall:
# rm -rf  ~/efp
# sudo apt uninstall verilator
# sudo apt uninstall gtkwave
# IF YOU REALLY WANT: sudo apt uninstall make
# IF YOU REALLY WANT: sudp apt uninstall g++
