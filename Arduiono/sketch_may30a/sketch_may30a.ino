#include <Wire.h>                   //i2c통신을 사용하기 때문에 아두이노의 i2c 통신용 라이브러리가 필요
#include <Adafruit_GFX.h>           // adafruit의 그래픽 관련 라이브러리
#include <Adafruit_SSD1306.h>        // ssd1306 제어용 라이브러리
#include <Servo.h>

#define SCREEN_WIDTH 128              // OLED 디스플레이의 가로 픽셀수
#define SCREEN_HEIGHT 64              // OLED 디스플레이의 세로 픽셀수

#define OLED_RESET     4             // 리셋핀이 있는 oled의 리셋핀에 연결할 아두이노의 핀 번호, 리셋핀이 없는 모듈은 임의의 숫자를 넣어도 됨.

#define VOLUM A0
#define BUTTON A1
#define BUSSER 10
#define SERVO 11
#define LEDR A3
#define LEDG A2
#define LEDB 7
#define LEDY 6
#define LEDW 8

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);    // 디스플레이 객체 생성

int buttonState;
int volumVal;
bool audio = false;
Servo servo;
int ledv = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("===========");
  Serial.println("Program Started");
  Serial.println("Sensor: LM35");
  Serial.println("===========")  ;
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C))         
    Serial.println(F("SSD1306 Not Connected"));
  else
    Serial.println("SSD1306 Connected");

  servo.attach(SERVO);
  pinMode(VOLUM,INPUT);
  pinMode(BUTTON,INPUT);
  pinMode(BUSSER,OUTPUT);
  pinMode(LEDR,OUTPUT);
  pinMode(LEDG,OUTPUT);
  pinMode(LEDB,OUTPUT);
  pinMode(LEDY,OUTPUT);
  pinMode(LEDW,OUTPUT);
  display.clearDisplay();
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(BUTTON);
  volumVal = analogRead(VOLUM);

  servo.write(map(volumVal, 0, 1023, 30, 150));
  if (buttonState == HIGH)
  {
    if(audio == false)
      audio = true;
    else
      audio = false;
  }

  if (audio)
  {
    tone(BUSSER, volumVal);
  }
  else
  {
    noTone(BUSSER);
  }
  ledv = map(volumVal, 0, 1023, 0, 4);
  if (volumVal == 0)
  {
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDG, LOW);
    digitalWrite(LEDB, LOW);
    digitalWrite(LEDY, LOW);
    digitalWrite(LEDW, LOW);
  }
  else if (ledv == 0)
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, LOW);
    digitalWrite(LEDB, LOW);
    digitalWrite(LEDY, LOW);
    digitalWrite(LEDW, LOW);
  }
  else if (ledv == 1)
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, LOW);
    digitalWrite(LEDY, LOW);
    digitalWrite(LEDW, LOW);
  }
  else if (ledv == 2)
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
    digitalWrite(LEDY, LOW);
    digitalWrite(LEDW, LOW);
  }
  else if (ledv == 3)
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
    digitalWrite(LEDY, HIGH);
    digitalWrite(LEDW, LOW);
  }
  else
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
    digitalWrite(LEDY, HIGH);
    digitalWrite(LEDW, HIGH);
  }
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.setCursor(0,27);
  display.println(volumVal);
  display.display();
}
