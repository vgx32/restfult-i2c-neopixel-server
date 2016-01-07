
all: 
	scp server.py pi@192.168.1.32:~/code/python
	ssh pi@192.168.1.32 
	# "cd ~/code/python"
	 # &&	python server.py"
	
    
