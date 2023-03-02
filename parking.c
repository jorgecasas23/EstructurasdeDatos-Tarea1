#include <stdio.h>
/*Jorge Casas
Grupo A
Codigo: 8961470*/

//Punto 1//

void parking(){
    int i = 0, t, n;
    scanf("%d", &t);
    while (i < t){
        scanf("%d", &n);
        int x[n];
        int j = 0;
        while(j < n){
            scanf("%d", &x[j]);
            j++;
        }
        int mayor = x[0];
        int menor = x[0];
        for (int k = 0; k < n; k++){
            if (x[k] < menor){
                menor = x[k];
            }
            if (x[k] > mayor){
                mayor = x[k];
            }
            
        
        }
        i++;
        int output = (mayor - menor) * 2;
        printf("%d\n", output);
    }
    
}






int main(){

    parking();
    return 0;
}
