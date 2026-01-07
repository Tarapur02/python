#include <TinyGPSPlus.h>
#include <HardwareSerial.h>

TinyGPSPlus gps;
HardwareSerial GPSSerial(2);  // use UART2

const int GPS_RX = 16;  // ESP32 RX2 <--- GPS TX
const int GPS_TX = 17;  // ESP32 TX2 ---> GPS RX (optional)

String nmeaLine = "";   // to capture raw NMEA for GST/GBS/ZDA, etc.

void setup() {
  Serial.begin(115200);
  GPSSerial.begin(9600, SERIAL_8N1, GPS_RX, GPS_TX);
  Serial.println("GPS interface started...");
}

void loop() {
  while (GPSSerial.available()) {
    char c = GPSSerial.read();

    // Feed character to TinyGPS++ parser
    gps.encode(c);

    // Build raw line to inspect any sentence (GST, GBS, ZDA, etc.)
    if (c == '\n') {
      // one full sentence received
      Serial.print("NMEA: ");
      Serial.print(nmeaLine);
      nmeaLine = "";
    } else if (c != '\r') {
      nmeaLine += c;
    }
  }

  // ----- RMC: time, date, position, speed, track -----
  if (gps.location.isUpdated()) {
    Serial.print("Lat: "); Serial.print(gps.location.lat(), 6);
    Serial.print("  Lon: "); Serial.println(gps.location.lng(), 6);
  }

  if (gps.speed.isUpdated()) {
    Serial.print("Speed: ");
    Serial.print(gps.speed.kmph());
    Serial.println(" km/h");
  }

  if (gps.course.isUpdated()) {
    Serial.print("Track: ");
    Serial.print(gps.course.deg());
    Serial.println(" deg");
  }

  if (gps.date.isUpdated() || gps.time.isUpdated()) {
    Serial.print("Date: ");
    Serial.print(gps.date.day()); Serial.print("/");
    Serial.print(gps.date.month()); Serial.print("/");
    Serial.println(gps.date.year());

    Serial.print("Time (UTC): ");
    Serial.print(gps.time.hour()); Serial.print(":");
    Serial.print(gps.time.minute()); Serial.print(":");
    Serial.println(gps.time.second());
  }

  // ----- GGA: altitude, satellites, fix quality -----
  if (gps.altitude.isUpdated() || gps.satellites.isUpdated()) {
    Serial.print("Satellites used: ");
    Serial.println(gps.satellites.value());

    Serial.print("Altitude: ");
    Serial.print(gps.altitude.meters());
    Serial.println(" m");
  }

  delay(500);
}
