float numero = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Vamos calcular a tabuada de um número!");
}

void loop() {
  Serial.println("Por favor, me diga um número para calcular a tabuada.");
  if(Serial.available()) {
    numero = Serial.parseFloat();
    delay(1000);

//eu quero deixar o "multiplicador" ao invés de "i" fica mais claro.
    for(float multiplicador = 0; multiplicador <= 10; ++multiplicador) {
      Serial.println(String(numero)+ 'x' +String(multiplicador)+ " = " +numero * multiplicador);
    }
  }
}
