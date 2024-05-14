package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Función para verificar si un número es primo
func esPrimo(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	// Pedir al usuario que ingrese números
	fmt.Print("Ingrese números separados por comas: ")
	var input string
	fmt.Scanln(&input)

	// Convertir la entrada del usuario en un array de números
	numerosStr := strings.Split(input, ",")
	var numeros []int
	for _, numeroStr := range numerosStr {
		numero, err := strconv.Atoi(strings.TrimSpace(numeroStr))
		if err != nil {
			fmt.Println("Error al convertir la entrada del usuario en números:", err)
			return
		}
		numeros = append(numeros, numero)
	}

	// Encontrar e imprimir números primos
	for _, numero := range numeros {
		if esPrimo(numero) {
			fmt.Println(numero)
		}
	}
}
