import paho.mqtt.client as mqtt
import pandas as pd
import csv
import codecs
import json

_g_cst_ToMQTTTopicServerIP = "localhost"
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName = "123" #TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)

fname = '20180306-modi01.csv'

with codecs.open(fname, "r", encoding='utf-8', errors='ignore') as csvf:
    for line in csv.DictReader(csvf):
        #print(json.dumps(line))
        lines={'Metric':dict(line)}
        mqttc.publish(_g_cst_MQTTTopicName, json.dumps(lines))

#mqttc.publish(_g_cst_MQTTTopicName, ass)
