#include <iostream>
#include<fstream>  
#include<windows.h> 
#include<conio.h>
#include<string>
#include <sstream>
#include <ctime>  //librerias necesarias para el funcionamiento del codigo 

using namespace std;//acceso a espacio de nombres

int main (){//funcion principal
		ofstream esc;//libreria para ingresar contenido en un fichero
		ifstream leer; //leer fichero
		int ope; //prototipos de funcion
		int menu();
		int menu2();
		void agregar(ofstream & esc);
		void verRegistros(ifstream & leer);
		void solicitarlibro(ifstream & leer);
		void agregarlibrofisico(ofstream & esc);
		void verRegistrosfisicos(ifstream & leer);
		void solicitarsalidafisica (ofstream & esc);
		void verlibrosprestados(ifstream & leer);//prototipos de funcion
			string w;// declarando variable como ("cadena de caracteres") 
	system("color 70");//cambiar color de consola
	system("cls");//borrar consola
cout<<"   ____________________________________________________"<<endl;
cout<<"  |                                                    |"<<endl;
cout<<"  |       B I B L I O T E C A     V I R T U A L        |"<<endl;
cout<<"  |____________________________________________________|"<<endl;
cout<<"  | __     __   ____   ___ ||  ____    ____     _  __  |"<<endl;
cout<<"  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |"<<endl;
cout<<"  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |"<<endl;
cout<<"  ||  |##||  | | || | |c++|||-|  | |==|+|+||-|-|~||__| |"<<endl;
cout<<"  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|"<<endl;
cout<<"  ||_______________________||__________________________|"<<endl;
cout<<"  | _____________________  || ___  __   __  _  __    _ |"<<endl;
cout<<"  ||=|=|=|=|=|=|=|=|=|=|=| || |=| |  |_|  ||#||==|  / /|"<<endl;
cout<<"  || | | | | | | | | | | | || | | |++|=|  || ||==| / / |"<<endl;
cout<<"  ||_|_|_|_|_|_|_|_|_|_|_|_||_|_|_|__|_|__||_||__|/_/__|"<<endl; 
cout<<"  |________________________||__________________________|"<<endl;
cout<<"  |________________________||         __   _ _   __    |"<<endl;
cout<<"  |___  __   __  _  ______ ||   |  | | _  | V | |__|   |"<<endl;
cout<<"  ||=| |  |_|  ||#||==|++| ||   |__| |__| |   | |  |   |"<<endl;
cout<<"  || | |++|=|  || ||==|  | ||       -usuario           |  "<<endl;
cout<<"  ||_|_|__|_|__||_||__|__|_||       -administrador     |"<<endl;
cout<<"  | _____   _  ____   ____ ||__________________________|"<<endl;
cout<<"  ||_____|_| |_|##|_|_|==|_|||+| | | |=|_|==|_|++|_|-|||"<<endl;
cout<<"  ||______||=|#|--| | |  | ||| | | | | | |  |~|  | | |||"<<endl;
cout<<"  ||______||_|_|__|_|_|__|_|||_|_|_|_|_|_|__|_|__|_|_|||"<<endl;
cout<<"  |________________________||__________________________|"<<endl;
cout<<"  |      _  /    ________     ________         /| _ _ _|"<<endl;
cout<<"  |    _|=|/   //    /| //   /  /  / |        / ||%|%|%|"<<endl;
cout<<"  |   |+|*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|"<<endl;
cout<<"  |   | |/   /(____|/ //                    /  /||~|~|~|"<<endl;
cout<<"  |___|_/   //______ //   _______          /  / ||_|_|_|"<<endl;
cout<<"  |___ /   (|______|//   |\_______)        /  /| ||_____|"<<endl;
cout<<"      /                  \|________)      /  / | |"<<endl;
	cout<<"ingrese su clave de usuario: "; 
	cin>>w;
// grafico de portada (entrada y salida)
	if (w=="admin"){ // condicion if (condicionales)
		do{          //ciclo do }while (ciclos) 
			system("cls");  
		ope=menu();	//se aigno la funcion menu() a la variable ope
			switch (ope){ //switch con el menu para llamar funciones segun el usuario elija
				case 1: //opciones del switch
						agregar(esc);	//funciones
				break;
				
			    case 2: 
			    		verRegistros(leer);
				break;
				
				case 3:
					    solicitarlibro(leer);
				break;
				
				case 4:
					    agregarlibrofisico(esc);
				break;
				
				case 5:
					verRegistrosfisicos(leer); 
				break;
				
				case 6:
					   solicitarsalidafisica(esc);
				break;	    
				case 7:
					   verlibrosprestados(leer); //funciones
				break;
			}
	}while(ope!=8); //cierre del do while
	
	
	    getch();
		return 0;
}else if (w!="admin"){ //condicion para el usuario
esc.open("archivo de salida de libros.txt", ios :: out | ios :: app ); //guardar en registro de libros prestados el nombre de usuario
esc<<"nombre de usuario registrado: "<<endl<<w;
esc.close();

		do{
			system("cls");  
		ope=menu2();	
			switch (ope){
				case 1:
						verRegistros(leer);
				break;
				
			    case 2: 
					    solicitarlibro(leer);
			    		
				break;
				
				case 3:
					
					verRegistrosfisicos(leer); 
				break;
				
				case 4:
					   solicitarsalidafisica(esc);
					    
				break;
				
			}
	}while(ope!=5); 
	
	
	    getch();
		return 0;
	}
	else{
	cout<<"usuario denegado vuelva a intentarlo"<<endl;
	system("pause");
}

}

int menu (){ //menu para el administrador
int a;
	system("color 03");
	system("cls");
cout<<"______________________________________________________________"                    <<endl;
cout<<"|  __   __    _ _  O      O ___ ___  __   __   __    __   __  |"                    <<endl;
cout<<"| |__| |  \\  | V | | |\\ | | |__  |  |__| |__| |  \\  |  | |__| |"                    <<endl;
cout<<"| |  | |__/  |   | | | \\| | ___| |  |  \\ |  | |__/  |__| |  \\ |"                    <<endl;
cout<<"|_____________________________________________________________|"                    <<endl;	
cout<<"|       .--.            .---.   |                             |"                    <<endl;             
cout<<"|   .---|__|    .-.     |s  |   |      O P C I O N E S        |"                    <<endl;
cout<<"|.--|===|--|    |_|     |i  |--.|____________________________ |"                    <<endl;
cout<<"||  |===|  |.---!~|  .--|s  |--|| 1)agregar libro digital     |"                    <<endl;
cout<<"||c |   |  ||===| |--|U |t  |  || 2)ver libros digitales      |"                    <<endl;
cout<<"||++|   |  ||   | |__|G |e  |  || 3)solicitar libro digital   |"                    <<endl;
cout<<"||  |   |  ||===| |==|M |m  |  || 4)agregar libro fisico      |"                    <<endl;
cout<<"||  |   |__||   |_|__|A |a  |__|| 5)ver registros fisicos     |"                    <<endl;
cout<<"||  |===|--||===|~|--|  |s  |--|| 6)solicitar libro fisico    |"                    <<endl;
cout<<"|^--^---'--^`---^-^--^--^---'--'| 7)ver libros prestados      |"                    <<endl;
cout<<"|       BIBLIOTECA VIRTUAL      | 8)salir                     |"                    <<endl;
cout<<"|_______________________________|_____________________________|"                    <<endl;
	cout<<"ingrese la opcion desea con su respectivo numero : "<<endl; 
	cin>>a;

return a;
	}
	
	int menu2 (){ //menu para el usuario
		system("COLOR 06");
	int a;//variable para guardar resultado de opcion elegida por el usuario 
	system("cls");  
	cout<<"   ____________________________________________________"<<endl;
cout<<"  |____________________________________________________|"<<endl;
cout<<"  | __     __   ____   ___ ||  ____    ____     _  __  |"<<endl;
cout<<"  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |"<<endl;
cout<<"  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |"<<endl;
cout<<"  ||  |##||  | | || | |c++|||-|  | |==|+|+||-|-|~||__| |"<<endl;
cout<<"  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|"<<endl;
cout<<"  ||_______________________||__________________________|"<<endl;
cout<<"  | _____________________  || ___  __   __  _  __    _ |"<<endl;                                                 
cout<<"  ||=|=|=|=|=|=|=|=|=|=|=| || |=| |  |_|  ||#||==|  / /|"<<endl;                           
cout<<"  || | | | | | | | | | | | || | | |++|=|  || ||==| / / |"<<endl;
cout<<"  ||_|_|_|_|_|_|_|_|_|_|_|_||_|_|_|__|_|__||_||__|/_/__|"<<endl; 
cout<<"  |________________________||__________________________|"<<endl;
cout<<"  ||       Universidad Gran Mariscal de Ayacucho      ||"<<endl;
cout<<"  ||              __         __   __   O   __         ||"<<endl;
cout<<"  ||       |  |  |__  |  |  |__| |__|  |  |  |        ||"<<endl;
cout<<"  ||       |__|  ___| |__|  |  | |  \\  |  |__|        ||  "<<endl;
cout<<"  ||_______________________  _________________________||"<<endl;
cout<<"  | _____   _  ____   ____ ||__________________________|"<<endl;
cout<<"  ||_____|_| |_|##|_|_|==|_|||+| | | |=|_|==|_|++|_|-|||"<<endl;
cout<<"  ||______||=|#|--| | |  | ||| | | | | | |  |~|  | | |||"<<endl;
cout<<"  ||______||_|_|__|_|_|__|_|||_|_|_|_|_|_|__|_|__|_|_|||"<<endl;
cout<<"  |________________________||__________________________|"<<endl;
cout<<"  |      _  /             OPCIONES             /| _ _ _|"<<endl;
cout<<"  |    _|=|/ 1)ver inventario                 / ||%|%|%|"<<endl;
cout<<"  |   |+|*/ 2)solicitar libro digital        /  ||=|=|=|"<<endl;
cout<<"  |   | |/ 3)ver registros fisicos          /  /||~|~|~|"<<endl;
cout<<"  |___|_/ 4)solicitar libro fisico         /  / ||_|_|_|"<<endl;
cout<<"  |___ / 5)salir                          /  /| ||_____|"<<endl;
cout<<"      /                                  /  / | |"<<endl;
cout<<"opcion a elegir: "; cin>>a; //pedir al usuario elegir opcion
	return a; //cuando la funcion sea llamada devolvera el valor guardado en a
	
}
	
	void agregar(ofstream & esc){ //declaracion de funcion
		system("cls");  
		string nom,code,preci;//variables como cadena de caracteres string
		esc.open("archivo generado.txt", ios :: out | ios :: app ); //crear y abrir archivo de texto con entrada y salida
		cout<<"nombre de libro: "; //permitir al usuario ingresar y guardar informacion en el archivo
		cin.ignore();//ignorar espacios en blanco
        getline(cin,nom);//guardar respuesta de usuario en variable nom
		cout<<"codigo de libro: "; cin>>code; 
		esc<<endl<<nom<<endl<<"codigo del libro:"<<code<<" "<<"\n"<<"------------------"<<endl; 
		esc.close();
		cout<<"ahora ingrese el libro  "<<nom<<"  en la carpeta de libros"<<endl<<"con el codigo "<<code<<" como nombre"<<endl;//indicarle a usuario como guardar libro
		system("pause"); //no permitir que el programa se cierre hasta presionar una tecla
	}
	
	void verRegistros(ifstream & leer){ //declaracion de funcion 
  			string text;
		  leer.open("archivo generado.txt",ios::in);//abrir y leer el registro
  		while(!leer.eof()){ //ciclo para leer todo hasta finalizar
  			getline(leer,text); //pasa el contenido del archivo a la variable text
  			cout<<text<<endl; //muestra el contenido de text
  			
		  } //cierre del ciclo 
  
  			system("pause"); //pausar hasta presionar otra tecla
  		leer.close();  //cierra el archivo
} //fin de la funcion 
	
	void solicitarlibro(ifstream & leer){ //entrada y salida 
	string text; // se define de variable como string  
	int a; // definir variable a como entero 
	system("cls"); //borrar pantalla
  			cout<<"libros disponibles digitalmente en formato (PDF)"<<endl; //titulo impreso en pantalla
		  leer.open("archivo generado.txt",ios::in); // archivo generado se abre como archivo de lectura 
  		while(!leer.eof()){ //se va a leer hasta que el archivo llegue a su fin  
  			getline(leer,text); //guardar el archivo en la variable text
  			cout<<endl<<text<<endl; //mostrar lo guardado en variable text
  			
		  }
  		leer.close();
  	
	cout<<"codigo del libro que desea ver: "<<endl; //darle a seleccionar al usuario
	cin>>a;//guardar respuesta del usuario en variable a
    
	 stringstream comando;// dictaminar comando como cadena de manejo de fflujo
	 comando<< "start libros\\"<<a<<".pdf"; // abre el PDF de la carpeta libros/
	   system(comando.str().c_str());// llamar con direccion variable con (system (comando para consola) 
    system("pause"); 
  	
	}
	
	
		void agregarlibrofisico(ofstream & esc){  // crear registro de libros fisicos 
		system("cls");  
		string nom,code;
		esc.open("archivo generado libros fisicos.txt", ios :: out | ios :: app );
		cout<<"nombre de libro: "; 
		cin.ignore();
        getline(cin,nom);
		cout<<"codigo de libro: "; cin>>code;
		esc<<nom<<endl<<"codigo del libro:"<<code<<endl<<"------------------"<<endl; //guardar informacion en el archvio apuntando a el  
		esc.close();
		 
	}
	
	    
		void verRegistrosfisicos(ifstream & leer){ //leer registro de libros fisicos 
  			string text;
		  leer.open("archivo generado libros fisicos.txt",ios::in);
  		while(!leer.eof()){
  			getline(leer,text);
  			cout<<text<<endl;
  			
		  }
  
  			system("pause");
  		leer.close();
  }

  void solicitarsalidafisica (ofstream & esc){
        	system("cls");   
		  char* dS[7] = {"Domingo","Lunes","Martes","Miercoles", "Jueves","Viernes","Sabado"}; //arreglo con dias de la semana para estructura de fecha
		time_t tSac = time(NULL);       // instante actual
   struct tm* tmP = localtime(&tSac); //estructura para fecha
		
		string nom,nro,code; 
		esc.open("archivo de salida de libros.txt", ios :: out | ios :: app );
		cout<<"nombre del solicitante: "; 
		cin.ignore();
        getline(cin,nom);;
		cout<<"numero de tlf "; cin>>nro;
		cout<<"escanee codigo del libro a llevarse: ";
		cin.ignore();
		getline(cin,code);
		esc<<endl<<"nombre de el solicitante: "<<endl<<nom<<endl<<"numero para localizar al solicitante :"<<endl<<nro<<" "<<"\n"<<"codigo del libro que posee :"<<code<<endl
		<<"dia de salida de este libro "<< tmP->tm_mday << "-" << tmP->tm_mon+1 << "-"<< tmP->tm_year+1900 <<" "<< dS[tmP->tm_wday] << endl<<
		"el dia de entrega de este libro es : "<<tmP->tm_mday+3<< "-" << tmP->tm_mon+1<< "-"<< tmP->tm_year+1900 << endl<<
		"------------------------------------------------"<<endl; //guardas datos registrados de salida y estructura de fecha en texto apuntando todos los datos a esc
		
		esc.close();
		system("pause"); 
	}
   
	void verlibrosprestados(ifstream & leer){ //leer registros 
  			string text;
		  leer.open("archivo de salida de libros.txt",ios::in);
  		while(!leer.eof()){
  			getline(leer,text);
  			cout<<text<<endl;
  			
		  }
  
  			system("pause");
  		leer.close();
}
	


