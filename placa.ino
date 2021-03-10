void setup()
   {

       Serial.begin(500000);
      
   }
void loop(){
  
  float t0a=0;
  float t1a=0;
  float t2a=0;
  float t3a=0;
  float t4a=0;
  float t5a=0;
  float t6a=0;
  float t7a=0;
  float t8a=0;
  float t9a=0;
  int n=0;
  
  while(n<10){ //la finalidad es sacar el promedio de 10 mediciones para una mayor exactitud
      float in0=analogRead(A11); //Aqui se toman las mediciones 0-1023
      //delay(100);
      float in1=analogRead(A15);
      //delay(100);
      float in2=analogRead(A12);
      //delay(100);
      float in3=analogRead(A14);
      //delay(100);
      float in4=analogRead(A0);
      //delay(100);
      float in5=analogRead(A1);
      //delay(100);
      float in6=analogRead(A3);
      //delay(100);
      float in7=analogRead(A5);
      //delay(100);
      float in8=analogRead(A7);
      //delay(100);
      float in9=analogRead(A9);
      //delay(100);
  
      float t0=(-0.157*in0)+155.7; //aqui se transforma a temperatura celcius
      float t1=(-0.157*in1)+155.7;
      float t2=(-0.157*in2)+155.7;  
      float t3=(-0.157*in3)+155.7;
      float t4=(-0.157*in4)+155.7;
      float t5=(-0.157*in5)+155.7;
      float t6=(-0.157*in6)+155.7;
      float t7=(-0.157*in7)+155.7;
      float t8=(-0.157*in8)+155.7; 
      float t9=(-0.157*in9)+155.7; 

      t0a=t0a+t0;  //aqui se suman 
      t1a=t1a+t1;
      t2a=t2a+t2;
      t3a=t3a+t3;
      t4a=t4a+t4;
      t5a=t5a+t5;
      t6a=t6a+t6;
      t7a=t7a+t7;
      t8a=t8a+t8;
      t9a=t9a+t9;

      n=n+1;
      //delay(100);

  }


  float t0f=t0a/10;
  float t1f=t1a/10;
  float t2f=t2a/10;
  float t3f=t3a/10;
  float t4f=t4a/10;
  float t5f=t5a/10;
  float t6f=t6a/10;
  float t7f=t7a/10;
  float t8f=t8a/10;
  float t9f=t9a/10;

Serial.print(" t0f");
Serial.print(t0f);

Serial.print(" t1f");
Serial.print(t1f);

Serial.print(" t2f");
Serial.print(t2f);

Serial.print(" t3f");
Serial.print(t3f);

Serial.print(" t4f");
Serial.print(t4f);

Serial.print(" t5f");
Serial.print(t5f);

Serial.print(" t6f");
Serial.print(t6f);

Serial.print(" t7f");
Serial.print(t7f);

Serial.print(" t8f");
Serial.print(t8f);

Serial.print(" t9f");
Serial.print(t9f);

Serial.print("\n");
    
    
    
    }
