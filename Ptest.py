!apt-get update                                                                          
!apt-get install openjdk-8-jdk-headless -qq > /dev/null                                  
!wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz 
!tar xzvf spark-3.1.2-bin-hadoop2.7.tgz                                                  
!pip install -q findspark==1.3.0        