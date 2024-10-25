#include "arduinoFFT.h" // importa a biblioteca da transformada de fourier

int SAMPLES=512;//const int SAMPLES = 512;             //numero de amostras,deve ser uma potência de 2 (2^n)
#define SAMPLING_FREQUENCY 10000 //Hertz, deve ser menor que 10000 devido ao conversor do arduino

/*const unsigned char PS_16=(1<<ADPS2);
const unsigned char PS_32=(1<<ADPS2)|(1<<ADPS0);
const unsigned char PS_64=(1<<ADPS2)|(1<<ADPS1);
const unsigned char PS_128=(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);*/

arduinoFFT FFT = arduinoFFT(); //cria o objeto FFT

unsigned int sampling_period_us;//variável para definir o tempo entre cada medição
unsigned long microseconds;//variável para a contagem do tempo
unsigned long tempo;
double vReal[4096];
double vImag[4096];
byte opcao;
int N,escolha=1;
int i,j,k;
float kk;
int apodizacao[] = {FFT_WIN_TYP_RECTANGLE,FFT_WIN_TYP_HAMMING,FFT_WIN_TYP_HANN,FFT_WIN_TYP_TRIANGLE,FFT_WIN_TYP_NUTTALL,
        FFT_WIN_TYP_BLACKMAN,FFT_WIN_TYP_BLACKMAN_NUTTALL,FFT_WIN_TYP_BLACKMAN_HARRIS,FFT_WIN_TYP_FLT_TOP,FFT_WIN_TYP_WELCH};
void setup() {
  Serial.begin(115200);
  sampling_period_us = round(1000000 * (1.0 / SAMPLING_FREQUENCY));
  analogReadResolution(12);
 /* ADCSRA &=~PS_128; //Limpa o Prescaler
  //ADCSRA |= PS_128; //128 Prescaler // DEFAULT
  //ADCSRA |= PS_64; //64 Prescaler
  //ADCSRA |= PS_32; //32 Prescaler
  ADCSRA |= PS_16; //16 Prescaler*/
}

void loop() {
  if (Serial.available() > 0) {
    opcao = Serial.read();
  }
  switch (opcao) {
    case 'E':
      SAMPLES = Serial.parseInt();
      escolha = Serial.parseInt();
      Serial.print(SAMPLES);
      opcao = 100;
      break;
    case 'A':
    tempo = millis();
      if (Serial.available() > 0) {
        if (Serial.read() == 'C') {
          double vReal[4096];
          double vImag[4096];
          i = 0;
          j = 0;
          opcao = 100;
          break;
        }
      }
      /*SAMPLING*/
      for (i = 0; i < SAMPLES; i++)
      {
        microseconds = micros();    //Overflows after around 70 minutes!

        vReal[i] = analogRead(0);
        vImag[i] = 0;

        while (micros() < (microseconds + sampling_period_us)) {
        }
      }
      for(k=0;k < SAMPLES;k++){
        //Serial.print(, 1);
        kk = (k*0.1);// * 1.0 * SAMPLING_FREQUENCY);// / SAMPLES;//k * 0.0001;
        //kk = (1/kk)*20;
        Serial.print(kk,6);
        Serial.print(",");
        Serial.println(vReal[k]);
        
      }
      /*FFT*/
      /*filtros para a transformada de fourier
        FFT_WIN_TYP_RECTANGLE,FFT_WIN_TYP_HAMMING,FFT_WIN_TYP_HANN,FFT_WIN_TYP_TRIANGLE,FFT_WIN_TYP_NUTTALL,
        FFT_WIN_TYP_BLACKMAN,FFT_WIN_TYP_BLACKMAN_NUTTALL,FFT_WIN_TYP_BLACKMAN_HARRIS,FFT_WIN_TYP_FLT_TOP,FFT_WIN_TYP_WELCH*/
      
      FFT.Windowing(vReal, SAMPLES, apodizacao[escolha], FFT_FORWARD);//aplicação de um filtro
      FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD); //transformada de fourier
      FFT.ComplexToMagnitude(vReal, vImag, SAMPLES); // cálculo do módulo do número complexo
      //double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQUENCY); // retorna o maior valor de amplitude do sinal analisado

      /*PRINT RESULTS*/
      //Serial.println(peak);     //imprime a frequência mais dominante

      for (j = 0; j < (SAMPLES / 2); j++)
      {

        Serial.print((j * 1.0 * SAMPLING_FREQUENCY) / SAMPLES, 1);
        Serial.print(",");
        Serial.print(vReal[j],1);//sqrt(pow(vReal[i],2)+pow(vImag[i],2)), 1);
        Serial.print("\n");
    
      }
      //Serial.println(millis()-tempo);
      opcao = 100;
      break;
  }
  
}
