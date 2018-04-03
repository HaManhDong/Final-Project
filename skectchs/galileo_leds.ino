#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.
byte mac[]    = {  0x98, 0x4F, 0xEE, 0x03, 0x14, 0xF4 };
IPAddress mqtt_server(10, 42, 0, 1);

int green_led = 2;
int red_led = 3;
int yellow_led = 4;
int blue_led = 5;

const char* yellow_topic = "pas/mqtt/led/yellow";
const char* blue_topic = "pas/mqtt/led/blue";
const char* user_scan_topic = "pas/mqtt/rfid/user_scan";


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println(topic);

  if (strcmp(topic, user_scan_topic) == 0) {
    digitalWrite(green_led, LOW);
    digitalWrite(red_led, HIGH);
  }
  else if (strcmp(topic, yellow_topic) == 0) {
    digitalWrite(red_led, LOW);
    digitalWrite(yellow_led, HIGH);
    delay(3000);
    digitalWrite(yellow_led, LOW);
    digitalWrite(green_led, HIGH);
  }
  else if (strcmp(topic, blue_topic) == 0) {
    digitalWrite(red_led, LOW);
    digitalWrite(blue_led, HIGH);
    delay(3000);
    digitalWrite(blue_led, LOW);
    digitalWrite(green_led, HIGH);
  }
}

EthernetClient ethClient;
PubSubClient client(ethClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("arduinoClient")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      // client.publish("dong","hello dong");
      // ... and resubscribe
      client.subscribe(yellow_topic);
      client.subscribe(blue_topic);
      client.subscribe(user_scan_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 3 seconds");
      // Wait 3 seconds before retrying
      delay(3000);
    }
  }
}

void setup()
{
  Serial.begin(115200);
  pinMode(green_led, OUTPUT);
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(blue_led, OUTPUT);

  digitalWrite(green_led, HIGH);

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  Ethernet.begin(mac);
  // Allow the hardware to sort itself out
  delay(1500);
}

void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
