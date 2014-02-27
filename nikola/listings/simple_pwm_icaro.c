/* 

Autor: Manuel Kaufmann
Email: humitos@gmail.com
License: GPL

Ejemplo sencillo que muestra el uso de senales PWM en el PIC18f4550
usando la placa ICARO (http://roboticaro.org/) en el PUERTO B.

Todas las salidas del PUERTO B tienen la misma frecuencia y el mismo
ciclo de trabajo. El ciclo de trabajo puede modificarse cambiando el
valor de ON_PERCENT, siendo este el porcentaje de tiempo en ALTO de la
salida del PUERTO B.

 */

#define USERINT 1  // define una interrupcion de usuario
#define TIMER 255  // valor del TIMER 0

#define ON_PERCENT 7 // ciclo de trabajo
                     // porcentaje del tiempo en ON

int count = 0;  // cantidad de veces que se entro en la userinterrupt()
                // este valor se compara contra ON_PERCENT para saber
                // si hay que poner la salida en 1 o 0


// funcion de configuracion
void setup()
{
  TRISB = 0;  // define a todos los pines del PUERTO B como salidas

  // configuracion de interrupciones
  INTCONbits.GIE = 1;  // habilita las interrupciones generales
  INTCONbits.TMR0IE = 1;  // habilita la interrupcion de TIMER 0

  // configuracion del TIMER 0
  T0CONbits.T08BIT = 1;  // usa 8 bits para el timer (2^8 = 256 posibilidades)
  T0CONbits.T0CS = 0;  // selecciona el modo TIMER
  T0CONbits.PSA = 1;  // (0) usa (1) no usa, un PRE SCALER previo

  TMR0L = TIMER;  // setea el valor del TIMER 0
  T0CONbits.TMR0ON = 1;  // arranca el TIMER 0
}


// bucle infinito
void loop()
{
  // no se necesita hacer nada en la funcion principal
  // todo se maneja desde las interrupciones
}


// funcion de interrupcion de usuario
void userinterrupt(void)
{
  if(INTCONbits.TMR0IF)  // chequea que la interrupcion sea del TIMER 0
                         // que es el que nos interesa
    {
      if(count < ON_PERCENT)
	{
	  PORTB = 0xFF;  // pone todas las salidas del PUERTO B en 1
	}
      else
	{
	  PORTB = 0x00;  // pone todas las salidas del PUERTO B en 0
	}

      count = ++count % 100; // comprueba si count es igual a 100, de ser asi
                             // vuelve su valor a 0 para volver a empezar

      INTCONbits.TMR0IF = 0;  // vuelve a 0 el FLAG de la interrupcion
                              // del TIMER 0
      TMR0L = TIMER;  // setea el valor del TIMER 0
    }
}
