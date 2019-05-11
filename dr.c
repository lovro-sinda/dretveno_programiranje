#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
int a=0;
void *dretva(int n)
{
        //printf("Ja sam dretva broj %d:  a=%d\n",n,a);
        if(n%3==0) sleep(1);
	a=a+1;
        //printf("Dretva broj %d je gotova...a=%d \n",n,a);

}

int main (void)
{
        int i, j;
        pthread_t t[10];

        for( i=0; i < 10; ++i)
        {
                if( pthread_create( &t[i],NULL, dretva,i))
                {
                        printf("Ne mogu stvoriti dretvu\n");
                }
        }
        for(j=0; j < 10;++j)
        {
                pthread_join(t[j],NULL);
        }
printf("%d\n",a);
return 0;
}

