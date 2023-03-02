#include <stdio.h>
/*Jorge Casas
Grupo A
Codigo: 8961470*/
void nlogonia(){
    int k, flag = 1, n, m;
    scanf("%d", &k);
    while (k != 0 && flag == 1){
        int j = 0;
        scanf("%d", &m);
        scanf("%d", &n);
        while (j < k && k < 1000 && flag){
            int x, y;
            scanf("%d", &x);
            scanf("%d", &y);
            if (x > m && y > n){
                printf("NE\n");
            }
            else if (x < m && y > n){
                printf("NO\n");
            }
            else if (x < m && y < n){
                printf("SO\n");
            }
            else if (x > m && y < n){
                printf("SE\n");
            }
            else if (y == n || x == m){
                printf("divisa\n");
            }
            j++;
        }
        scanf("%d", &k);
    }
}    


int main(){
    nlogonia();
    return 0;
}