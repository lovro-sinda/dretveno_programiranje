#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <inttypes.h> 
typedef unsigned long long ll;

#define NAJVECI_BROJ 0xffffffffffffffffULL
#define KRAJ_RADA 1
#define NIJE_KRAJ 0
#define MAX_DIVISOR 150000
#define MAX_ITER 18000000
#define A 8531648002905263869ULL
#define B 18116652324302926351ULL
#define LEN 6

struct MS{
    ll broj;
    char done;
};
typedef struct MS MS;
MS arr[LEN];
int pokazivac1 = 0;
int pokazivac2 = 0;

long int lastCheck = 0;
long int firstTime = 0;

int test_pseudo_prost(ll x) {
    if(x == 1) return 0;
    for(int i = 3;i <= MAX_DIVISOR; i += 2) {
        if(x % i == 0) return 0;
    }
    return 1;
}

int test_bitovi(ll x) {
    int pocJedinica = 0;
    for(int i=0;i<63;++i) {    
        if((x & (1ULL<<i)) != 0) {
            pocJedinica = i;
            break;
        }
    }
    for(int i=pocJedinica+1;i<63;++i) {
        ll o1 = x & ((1ULL<<(i-1)));
        ll o2 = x & ((1ULL<<(i)));
        ll o3 = x & ((1ULL<<(i+1)));
        if( o1 != 0 & o2 != 0 && o3 != 0)
            return 0;
        if( o1 == 0 && o2 == 0 && o3 == 0) 
            return 0;
    }
    return 1;
}
ll rnd;

ll pseudo_64broj() {
    rnd = (rnd * A) % B;
    return rnd;
}

int provjera_zahtjeva() {
    if(time(0) - lastCheck < 1) {
        // nije prošla 1 sekunda
        return NIJE_KRAJ;
    } else {
        int r1 = rand() % 100;
        if( r1 < 50 && arr[pokazivac2].done == 0 ) {
            printf("%03ld - MS[] = {",time(0) - firstTime);    

            arr[pokazivac2].done = 1;
            pokazivac2 = (pokazivac2 + 1) % LEN;
            for(int i = 0; i < LEN; ++i) {
                printf("%d. %02llx ", i, arr[i].broj % 100);            
            }
            printf("} I=%d, U=%d, ", pokazivac2, pokazivac1);
            printf("MS[i]= %llx\n",arr[pokazivac2].broj);
            lastCheck = time(0);
        } 
        if( r1 < 10) {
            return KRAJ_RADA;
        }
        else {
            return NIJE_KRAJ;
        }
    }
}

int main(void) {    
    rnd = time(0);
    firstTime = time(0);
    do {
        ll x = pseudo_64broj() | 1;
        int iter = 0;
        while( !test_bitovi(x) || !test_pseudo_prost(x)) {
            if( x <= NAJVECI_BROJ - 2 ) {
                x += 2;
            } else {
                x = pseudo_64broj() | 1;
            }
            if(++iter >= MAX_ITER) break;
        }
        // dodaj x u MS
        pokazivac1 = (pokazivac1 + 1) % LEN;
        arr[pokazivac1].broj = x;
        arr[pokazivac1].done = 0;

    } while( provjera_zahtjeva() != KRAJ_RADA);
        
    return 0;
}
