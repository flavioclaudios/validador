import streamlit as st

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(digito) * (peso - i) for i, digito in enumerate(cpf))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    return cpf[-2:] == digito1 + digito2

# Interface Streamlit
st.set_page_config(page_title="Validador de CPF", page_icon="🔍")
st.title("🔍 Validador de CPF")

cpf_input = st.text_input("Digite o CPF (com ou sem pontuação):")

if cpf_input:
    if validar_cpf(cpf_input):
        st.success("✅ CPF válido!")
    else:
        st.error("❌ CPF inválido.")