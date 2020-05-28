FROM sebp/elk

# specify custom logstash config
ADD cfg/logstash.conf /opt/logstash/config/logstash.conf