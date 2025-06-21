import random
import time


from paho.mqtt import client as mqtt_client




broker = 'broker.emqx.io'
port = 1883
topic = "IOT-24"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'publisher'
password = 'publisher'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client




def publish(client):
    msg='Welcome to IOT class 2024'
    while True:
        time.sleep(1)
        result = client.publish(topic, msg )
        status = result[0]
        if status == 0:
            print(f"Successfully sent message to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


        
        






def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)




if __name__ == '__main__':
    run()