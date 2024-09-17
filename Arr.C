#include<stdio.h>
void si_suma(int arr[]);

void si_suma(int arr[]){
	int const target = 9;
	for (int i=0; i < 8; i++)
	{
		for (int j=0; j < 8; j++)
		{
			int temp1, temp2;

			temp1 = arr[i];
			temp2 = arr[j];

			if (temp1 + temp2 == target){
				printf("%d %d\n",i,j);
			}
		}
	}
}

void main (){
	
	int arr[9] = {1,2,3,4,5,6,7,8,9};
	si_suma(arr);

}