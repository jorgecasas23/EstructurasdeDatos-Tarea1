#include <stdio.h>
/*Jorge Casas
Grupo A
Codigo: 8961470*/

//Punto 3//

void lock(){
    int n, comb1 = 1, comb2 = 1, comb3 = 1, sum;
    scanf("%d", &n);
    scanf("%d", &comb1);
    scanf("%d", &comb2);
    scanf("%d", &comb3);
    while (!(n == 0 && comb1 == 0 && comb2 == 0 && comb3 == 0)){
        sum = 0;
        sum += 1080;
        if (comb1 > n){
            sum += (40 - comb1 + n) * 9;
        }
        else{
            sum += (n - comb1) * 9;
        }
        if (comb2 > comb1){
            sum += (comb2 - comb1)  * 9;
        }
        else{
            sum += (40 - comb1 + comb2) * 9;
        }
        if (comb3 > comb2){
            sum += (40 - comb3 + comb2) * 9;
        }
        else{
            sum += (comb2 - comb3) * 9;
        }
        printf("%d\n", sum);
        scanf("%d", &n);
        scanf("%d", &comb1);
        scanf("%d", &comb2);
        scanf("%d", &comb3);
    }
}

int main(){
    lock();
    return 0;
}