import streamlit as st

def calculator():
    st.title("Calculadora Simples")
    
    num1 = st.number_input("Digite o primeiro número:")
    num2 = st.number_input("Digite o segundo número:")
    
    operation = st.selectbox("Selecione a operação", ["Soma", "Subtração", "Multiplicação", "Divisão"])
    
    if st.button("Calcular"):
        if operation == "Soma":
            result = num1 + num2
            st.success(f"A soma de {num1} e {num2} é {result}.")
        elif operation == "Subtração":
            result = num1 - num2
            st.success(f"A subtração de {num1} e {num2} é {result}.")
        elif operation == "Multiplicação":
            result = num1 * num2
            st.success(f"A multiplicação de {num1} e {num2} é {result}.")
        elif operation == "Divisão":
            if num2 == 0:
                st.error("Impossível dividir por zero.")
            else:
                result = num1 / num2
                st.success(f"A divisão de {num1} por {num2} é {result}.")

if __name__ == "__main__":
    calculator()

