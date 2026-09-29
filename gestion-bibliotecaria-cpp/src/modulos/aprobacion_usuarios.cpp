#include<iostream>
#include<fstream>  
#include<windows.h> 
#include<conio.h>
#include<string>
#include <sstream>

using namespace std;

int main (){
		ofstream esc;
		ifstream leer; 
		int ope; 
		int menu();
		void agregar(ofstream & esc);
		void verRegistros(ifstream & leer);
		void solicitarlibro(ifstream & leer);
string w;
	system("color 70");
	system("cls");
cout<<"       .--.            .---."                         <<endl;             
cout<<"   .---|__|    .-.     |s  |"                       <<endl;
cout<<".--|===|--|    |_|     |i  |--."                    <<endl;
cout<<"|  |===|  |.---!~|  .--|s  |--|"                    <<endl;
cout<<"|c |   |  ||===| |--|U |t  |  |"                    <<endl;
cout<<"|++|   |  ||   | |__|G |e  |  |"                    <<endl;
cout<<"|  |   |  ||===| |==|M |m  |  |"                    <<endl;
cout<<"|  |   |__||   |_|__|A |a  |__|"                    <<endl;
cout<<"|  |===|--||===|~|--|  |s  |--|"                    <<endl;
cout<<"^--^---'--^`---^-^--^--^---'--'"                    <<endl;
	cout<<"ingrese su clave usuario: "<<endl; 
	cin>>w;

	if (w=="usuario"){
		do{
			system("cls");  
		ope=menu();	
			switch (ope){
				case 1:
						agregar(esc);	
				break;
				
			    case 2: 
			    		verRegistros(leer);
				break;
				
				case 3:
					    solicitarlibro(leer);
				break;
			}
	}while(ope!=5); 
	
	
	    getch();
		return 0;
}else if (w=="admin"){
	cout<<"en progreso";
	//menu,funciones,todo lo que hara el administrador
	}
	else{
	cout<<"usuario denegado vuelva a intentarlo";
}

}

int menu (){
	system("color 70");
	int a;
	system("cls");  
	cout<<"                                                1 agregar libro\n";
	cout<<"                                                2 ver libros \n";
	cout<<"                                                3 solicitar libro\n";
	cout<<"                                                5 salir\n";
	cout<<"                                                opcion: ";
	cin>>a;
	return a;
	}
	
	void agregar(ofstream & esc){ 
		system("cls");  
		string nom,code,preci;
		esc.open("archivo generado.txt", ios :: out | ios :: app );
		cout<<"nombre de libro: "; 
		cin.ignore();
        getline(cin,nom);;
		cout<<"codigo de libro: "; cin>>code;
		esc<<nom<<endl<<"codigo del libro:"<<code<<" "<<"\n"<<"------------------"<<endl; 
		esc.close();
		cout<<"ahora ingrese el libro  "<<nom<<"  en la carpeta de libros"<<endl<<"con el codigo "<<code<<" como nombre"<<endl;
		system("pause"); 
	}
	
	void verRegistros(ifstream & leer){ 
  			string text;
		  leer.open("archivo generado.txt",ios::in);
  		while(!leer.eof()){
  			getline(leer,text);
  			cout<<text<<endl;
  			
		  }
  
  			system("pause");
  		leer.close();
  
  
  
  
}
	
	void solicitarlibro(ifstream & leer){
	string text;
	int a;
		  leer.open("archivo generado.txt",ios::in);
  		while(!leer.eof()){
  			getline(leer,text);
  			cout<<text<<endl;
  			
		  }
  
  			
  		leer.close();
  	
	cout<<"codigo del libro que desea ver: "<<endl;
	cin>>a;
    
	 stringstream comando;
	 comando<< "start libros\\"<<a<<".pdf";
	   system(comando.str().c_str());
    system("pause");
  	
	}


