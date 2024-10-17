#include <stdio.h>

int main() (
    int peso;
    float altura, imc;

    printf("Informe seu peso (em kgs):\n");
    scanf("%d", &peso);

    printf("Informe sua altura:\n");
    scanf("%f", &altura);

    imc = peso / (altura * altura);

    printf("\n\n Seu IMC = %.2f", imc);
    printf("\nClassificacao IMC");
    if (imc < 18.5)
        print("Abaixo do peso");
    else if ((imc >= 18.5) && (imc < 25))
            printf("Peso normal");
        else if ((imc >=25) && (imc < 30))
                printf("Acima do peso");
            else if ((imc >= 30) && (imc <34))
                    printf("Obeso");
        else
            printf("Muito obeso");
)