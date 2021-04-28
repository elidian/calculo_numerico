#include <stdio.h>
#include <math.h>

double f(double num){
    double result = num - log(pow(num, num));
    return result;
}

int main(){
    double aa=2, bb=3, erro=0.00001;
    double  kk = (log(bb-aa) - log(erro))/log(2);
    printf("interacoes K = %f\n", kk);
    int tam=kk;
    
    double a[tam], b[tam], x[tam];
    int k = 1;
    a[k] = aa;
    b[k] = bb;
    x[k] = (a[k]*fabs(b[k]) + b[k]*fabs(a[k]))/(fabs(b[k]) + fabs(a[k]));
    printf("interacao %d\n", k);
    printf("a[%d] = %f\n", k, a[k]);
    printf("x[%d] = %f\n", k, x[k]);
    printf("b[%d] = %f\n", k, b[k]);
    printf("f(x[%d]) = %f\n\n", k, f(x[k]));

    while (fabs(f(x[k])) > erro && k < tam){
        if (f(a[k])*f(x[k]) < 0) /* raiz em [ak , xk] */
        {
            //printf("A\n");
            a[k+1] = a[k];
            b[k+1] = x[k];
        }
        else /* raiz em [xk, bk] */
        {
            //printf("B\n");
            a[k+1] = x[k];
            b[k+1] = b[k];
        }
        k = k + 1;
        x[k] = (a[k]*fabs(b[k]) + b[k]*fabs(a[k]))/(fabs(b[k]) + fabs(a[k]));

        printf("interacao %d\n", k);
        printf("a[%d] = %f\n", k, a[k]);
        printf("x[%d] = %f\n", k, x[k]);
        printf("b[%d] = %f\n", k, b[k]);
        printf("F(x[%d]) = %f\n\n", k, f(x[k]));

    };
    if (k > tam)
        printf("parada falhou\n");
    else
        printf("Resultado x[%d]: %f\n", k, x[k]);
    
    return 0;
}