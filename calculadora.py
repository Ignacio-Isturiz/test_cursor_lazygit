#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sumar(a, b):
    """Función para sumar dos números"""
    return a + b

def restar(a, b):
    """Función para restar dos números"""
    return a - b

def main():
    print("=== Calculadora Simple ===")
    print("Funciones disponibles: suma y resta")
    
    # Ejemplos de uso
    num1 = 10
    num2 = 5
    
    print(f"Suma: {num1} + {num2} = {sumar(num1, num2)}")
    print(f"Resta: {num1} - {num2} = {restar(num1, num2)}")

if __name__ == "__main__":
    main() 