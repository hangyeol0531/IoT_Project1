
char ch;

void setup()
{
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if(Serial.available()){
    ch = Serial.read();
  }
  
  if(ch == '1'){                 //Red
       digitalWrite(11, HIGH);
    }else if(ch == '2'){
       digitalWrite(11, LOW);
    }else if(ch == '3'){        //Blue
       digitalWrite(13, HIGH);
    }else if(ch == '4'){
       digitalWrite(13, LOW);
    }else if(ch == '5'){        //Green
       digitalWrite(12, HIGH);
    }else if(ch == '6'){
       digitalWrite(12, LOW);
    }else if(ch == '7'){        //All
       digitalWrite(11, HIGH);
       digitalWrite(12, HIGH);
       digitalWrite(13, HIGH);
    }else if(ch == '8'){
       digitalWrite(11, LOW);
       digitalWrite(12, LOW);
       digitalWrite(13, LOW);
    }
}
