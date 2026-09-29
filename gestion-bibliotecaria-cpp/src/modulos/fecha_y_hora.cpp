#include <iostream>
#include<iostream>
#include<fstream>  
#include<windows.h> 
#include<conio.h>
#include<string>
#include <sstream>
#include <ctime>
using namespace std;


int main() {    
 ofstream esc;
   void agregar(ofstream & esc);        
 cout<<"hola";
agregar(esc);	
				

   return 0;
}

 void agregar(ofstream & esc){
        char* dS[7] = {"Domingo","Lunes","Martes","Miercoles", "Jueves","Viernes","Sabado"};
		time_t tSac = time(NULL);       // instante actual
   struct tm* tmP = localtime(&tSac);
   esc.open("archivo generado.txt", ios :: out | ios :: app );
		esc<<"dia mes año "<< tmP->tm_mday << "-" << tmP->tm_mon+1 << "-"<< tmP->tm_year+1900 << endl<< "Dia de semana: " << dS[tmP->tm_wday] << endl;
		
		esc.close();
		system("pause"); 
   }
   
