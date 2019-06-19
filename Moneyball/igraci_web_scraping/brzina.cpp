#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
struct par
{
	int uk;
	double koef;
        int pozicija;
};
int broj=0,c,a;
double b;
map <string,double> mapa1;
map <string,double> mapa2;
set <string> s;
vector <int> v;
par polje [20000];
int brojac=0;
par par;
int main()
{
	ifstream myfile;
	myfile.open("brzina.csv");

	while(myfile.good())
	{
		string line1;
		string line2;
		string line3;
		string line4;

		getline(myfile, line1, ',');
    		getline(myfile, line2,',');
		b=atoi(line1.c_str());
        a=atoi(line2.c_str());
    		getline(myfile, line3 );
		b=b*0.45359237;
		par.uk=a;
		par.koef=b;
		                    polje[brojac]=par;
		                  ++brojac; 
      
	/*	if(line3=="N"){    
                          polje[brojac]=par;
		                  ++brojac; 
                      }    	
    */    
    }
    printf("%d\n",brojac);
	myfile.close();
ofstream novifile;
novifile.open("koef.csv");
novifile << "overall" <<","<< "koef"<<endl;
    for(int i=0;i<brojac;++i)
    {
        novifile << polje[i].uk <<","<<polje[i].koef<<endl;    
    }
return 0;
}

