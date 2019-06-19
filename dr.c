#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
int a=0;
void *dretva(int n)
{
        //printf("Ja sam dretva broj %d:  a=%d\n",n,a);
        //if(n%3==0) sleep(1);
	for(int i=0;i<=10000;++i)
	{
	}
	a=a+1;
        //printf("Dretva broj %d je gotova...a=%d \n",n,a);

}

int main (void)
{
        int i, j;
        pthread_t t[1000];

        for( i=0; i < 1000; ++i)
        {
                if( pthread_create( &t[i],NULL, dretva,i))
                {
                        printf("Ne mogu stvoriti dretvu\n");
                }
        }
        for(j=0; j < 1000;++j)
        {
                pthread_join(t[j],NULL);
        }
printf("%d\n",a);
return 0;
}

