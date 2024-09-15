#include <ESP32Servo.h>

// 1) attachServo(pin);
// 2) setAngle(pin, angle);
// 3) setDebug(state);

#define SERVO_ARRAY_SIZE 40
Servo servos[SERVO_ARRAY_SIZE];

#define START_ARGS '('
#define END_ARGS ')'
#define ARG_SEPARATOR ','
#define END_COMMAND ';'
#define MAX_PARAM_STACK_SIZE 10

bool debug = true;

void attachServo(int pin) {
  if (debug) Serial.printf("attachServo(%d);\n", pin);
  if (pin < 0 || pin >= SERVO_ARRAY_SIZE) {
    Serial.println("Pin inválido");
    return;
  }
  servos[pin].attach(pin);
}

void setAngle(int pin, int angle) {
  if (debug) Serial.printf("setAngle(%d, %d);\n", pin, angle);
  if (pin < 0 || pin >= SERVO_ARRAY_SIZE) {
    Serial.println("Pin inválido");
    return;
  }
  if (angle < 0 || angle > 180) {
    Serial.println("Ángulo inválido");
    return;
  }
  servos[pin].write(angle);
}
void setDebug(bool state) {
  if (debug) Serial.printf("setDebug(%d);\n", state);
  debug = state;
}
void unknownCommand(String cmd, int* stack_begin, int* stack_end) {
  Serial.printf("Comando desconocido: %s;\n", cmd);
  if (debug) {
    Serial.print("Pila de argumentos: ");
    for (int* p = stack_begin; p < stack_end; p++)
      Serial.printf("%d ", *p);
    Serial.println();
  }
}

bool isNumeric(String str) {
  if (str.isEmpty()) return false;
  for (int i = 0; i < str.length(); i++) {
    if (str.charAt(i) < '0' || str.charAt(i) > '9') return false;
  }
  return true;
}

void processCommand() {
  String full_command = Serial.readStringUntil(END_COMMAND);
  if (full_command == NULL) return;
  int param_stack[MAX_PARAM_STACK_SIZE] = { 0 };
  int* stack_ptr = param_stack;
  int start_index = full_command.indexOf(START_ARGS);
  int end_index = full_command.indexOf(END_ARGS);
  if (start_index < 0 || end_index < 0) return;
  String args = full_command.substring(start_index + 1, end_index);
  int sep_index = 0;
  while (1) {
    sep_index = args.indexOf(ARG_SEPARATOR);
    if (sep_index < 0) {
      if (args.isEmpty()) break;
      else sep_index = args.length();
    };
    String arg = args.substring(0, sep_index);
    args = args.substring(sep_index + 1);
    arg.trim();
    if (!isNumeric(arg)) return;
    if (stack_ptr - param_stack >= MAX_PARAM_STACK_SIZE) return;
    *stack_ptr++ = arg.toInt();
  }
  String cmd = full_command.substring(0, start_index);
  cmd.trim();
  if (cmd.equals("attachServo")) {
    attachServo(param_stack[0]);
  } else if (cmd.equals("setAngle")) {
    setAngle(param_stack[0], param_stack[1]);
  } else if (cmd.equals("setDebug")) {
    setDebug(param_stack[0]);
  } else {
    unknownCommand(cmd, param_stack, stack_ptr);
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("TEST N°2 COMANDOS AVANZADOS");
  Serial.setTimeout(10);
}

void loop() {
  processCommand();
}
