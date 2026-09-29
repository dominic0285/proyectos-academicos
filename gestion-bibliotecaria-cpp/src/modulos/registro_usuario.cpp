#include<iostream>
#include<fstream>  
#include<windows.h> 
#include<conio.h>

using namespace std;

int menu (){
string w;
do{
	
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
  
	if(w=="admin"){

    int a;
	system("cls");  
	cout<<"                                                2 ver libros agregados\n";
	cout<<"                                                3 solicitar libro digital\n";
	cout<<"                                                4 registrar salida de libro\n";
	cout<<"                                                5 salir\n";
	cout<<"                                                opcion: ";
	cin>>a;
	return a;
	}
	else if(w=="usuario") {
		 int a;
	system("cls");  
	cout<<"                                                2 ver libros agregados\n";
	cout<<"                                                3 solicitar libro digital\n";
	cout<<"                                                4 solicitar libro fisico\n";
	cout<<"                                                5 salir\n";
	cout<<"                                                opcion: ";
	cin>>a;
	return a;
	}
		else{
		cout<<"usuario denegado";
		}	
	
}while(w=="admin"||w=="usuario");
}


	
		int main(){ 
		int ope; 
		do{
			system("cls");  
		ope=menu();	
			switch (ope){
				case 1:
					
				break;
				
			    case 2: 
			    		;
				break;
				
				case 3:
				
				break;
				
				case 4: 
				
				case 5: exit (0);
			}
	}while(ope!=5); 
	
	
	    getch();
		return 0;
}
