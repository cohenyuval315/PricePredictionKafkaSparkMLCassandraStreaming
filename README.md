# ONGOING
# TEMP: 
windows using wsl2:
1.powershell:
- Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0 
- notepad $env:USERPROFILE\.ssh\config
- ssh-keygen
- copy key

--- Pre ---:
all computers, using sudo apt-get , using documentation:
(versions compatability)
download kafka 
download spark 
download cassandra

--- windows ---:
enable desktop remote host
ip is default gateway in ethernet or wifi , ipv4
mstsc
settings for port
change wsl start to 127.rest of wsl2 Address
secpol.msc
local policies
user right assignment
https://www.anyviewer.com/how-to/remote-desktop-access-denied-2578.html#:~:text=Add%20your%20user%20into%20Remote,Remote%20Desktop%20Users%20local%20group.
--- WSL2 ---:
---
.bashrc/.zshrc 
export KAFKA_HOME=/path/kafka
export SPARK_HOME=/path/spark
export PATH=$PATH:$SPARK_HOME/bin:$KAFKA_HOME/bin
export PATH=$SPARK_HOME/sbin:$PATH
export PATH=$SPARK_HOME/bin:$PATH
- source bashrc / zshrc
---
---
-- Kafka --:
# change sh script to wsl from windows
sudo apt-get install dos2unix
dos2unix init/init_kafka.sh
./init/init_kafka.sh
kafka script run zookeeper and 1 kafka broker
-----------
---
-------------


Spark:
after copy
-as a worker spark-env.sh:
export SPARK_LOCAL_IP=ipconfig(wsl)(IPv4 Address)
export SPARK_MASTER_URL=spark://(master-ip)(x.x.x.x):7077(default-port)
export SPARK_WORKER_MEMORY=1g


Scala Program Main Computer:
- scala download (version fit to spark version , env)
- sbt download


ssh allow in windows
kafka,spark download
scala
