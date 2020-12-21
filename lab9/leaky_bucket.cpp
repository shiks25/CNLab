//Write a program for congestion control using Leaky bucket algorithm

#include<bits/stdc++.h>

using namespace std;

int bucketSize;

void delay(int delay) 
{ 
 int now=time(NULL); 
 int later=now+delay; 
 while(now<=later){
 now=time(NULL); 
 }
} 

void bktInput(int a,int b) {
 if(a>bucketSize) {
 	cout<<"\n\t\tBucket overflow";
 }
 else {
	 delay(1);
	 while(a>b){
		 cout<<"\n\t\t"<<b<<" bytes outputted.";
		 a-=b;
		 delay(1);
 	}
 	
  if(a>0) {
  	cout<<"\n\t\tLast "<<a<<" bytes sent\t";
  }
  
  cout<<"\n\t\tBucket output successful";
 }
 
}

int main() {
	 int op, pktSize;
	 cout<<"Enter Bucket Size: ";cin>>bucketSize;
	 cout<<"Enter output rate : "; cin>>op;
	 for(int i=1;i<=5;i++){
		 delay(1);
		 pktSize=rand() % 1000;
		 cout<<"\nPacket no. "<<i<<"\tPacket size = "<<pktSize;
		 bktInput(pktSize,op);
	 }
	 cout<<"\n";
	 return 0;
} 
