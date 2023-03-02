#include <stdio.h>
/*Jorge Casas
Grupo A
Codigo: 8961470*/

//Punto 5//

void finish(){
    int T, N, k = 1;
    scanf("%d", &T);
    while (k <= T && T <= 50){
        scanf("%d", &N);
        int p[N], q[N];
        int flag = 0;
        for (int i = 0; i < N; i++){
            scanf("%d", &p[i]);
        }
        for (int i = 0; i < N; i++){
            scanf("%d", &q[i]);
        }
        for (int i = 0; i < N && flag == 0; i++){
            if (p[i] - q[i] > 0 && flag == 0){
                printf("Case %d: Possible from station %d\n", k, (i+1));
                flag = 1;
            }
        }
        if (flag == 0){
            printf("Case %d: Not possible\n", k);
        }
        k++;
       
    }
}

int main(){
    finish();
    return 0;
}