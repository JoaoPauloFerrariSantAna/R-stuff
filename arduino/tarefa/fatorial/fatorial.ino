//para calcularmos o fatorial, irá ser necessário que o fatorial, inicialmente seja igual ao numero desejado...

float numero = 0;
float result = 1;

void setup() {
  Serial.begin(9600);
  Serial.println("Vamos calcular o fatorial!");
}

void loop() {
  Serial.println("Para começarmos, me dê um número.");
  if(Serial.available()) {
    numero = Serial.parseFloat();
    
//então fatorial = numero e fatorial > 0 porque <numero formado pelo fatorial> * 0 = 0, que anula a conta toda.
    for(float fatorial = numero; fatorial > 1; --fatorial) {
      result *= fatorial;

//o negócio é: eu não estou conseguindo mostrar só o último numero da conta, é por isso que só mostra a conta inteira. Mas os números estão certos
//eu iria conseguir mostrar só o resultado se eu pudesse deixar o código em uma função

      Serial.println(result);
    }
    result = 1;
  }
}
