import random
import string


from paho.mqtt import client as mqtt_client




broker = 'broker.emqx.io'
port = 1883
topic= "IOT-24"


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'subscriber'
password = 'subscriber'




def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION1)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client




def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        x=msg.payload.decode()
        print(x)


    client.subscribe(topic)
    client.on_message = on_message




def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()




if __name__ == '__main__':
    run()