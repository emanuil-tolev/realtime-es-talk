Install all the software under 1 dir, let's say "demo/"

First, let's setup the Python demo script.

    cd demo/
    virtualenv pydemo
    cd pydemo
    . bin/activate
    cp -r <talk repo>/pydemosrc src/
    cd src
    pip install -r requirements.txt
    python demo.py

This should be fetching data from the weather API. Now the rest of it.

1. cd elasticsearch-6.6.0 && ./bin/elasticsearch
2. cd kibana-6.6.0-darwin-x86_64 && ./bin/kibana
3. we will run logstash after everything else, don't run it yet
4. cd kafka_2.11-0.10.2.2 && bin/zookeeper-server-start.sh config/zookeeper.properties
5. cd kafka_2.11-0.10.2.2 && bin/kafka-server-start.sh config/server.properties
6. bin/logstash -e 'input { kafka { bootstrap_servers => "localhost:9092" topics => "weather" } } filter { json { source => "message"} } output { elasticsearch { hosts => ["localhost:9200"] index => "weather" } stdout {} }'
7. Open Kibana at localhost:5602 and explore at will
