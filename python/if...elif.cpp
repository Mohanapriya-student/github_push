#include<iostream>
using namespace std;
int main()
{
	int Electricity;
	cout<<"Enter your electricity unit:"<<endl;
	cin>>Electricity;
	if(Electricity<=100)
	{
		cout<<"Low usage"<<endl;
	}
	else if(Electricity>100&&Electricity<=200)
	{
		cout<<"Medium usage"<<endl;
	}
	else
	{
		cout<<"High usage";
	}
}
