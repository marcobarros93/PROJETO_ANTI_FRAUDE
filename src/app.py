import streamlit as st
from services.blob_service import upload_image_to_blob
from services.credit_card_service import analyze_credit_card
from utils.config import get_connection_string

# Função separada para exibir imagem e resultado da validação
def show_image_and_validation(image, validation_result):
    """Exibe a imagem enviada e o resultado da validação."""
    st.image(image, caption="Imagem enviada", use_column_width=True)
    st.write("### Resultado da análise:")
    st.json(validation_result)

# Título principal
st.title("Sistema de Detecção de Fraudes em Cartões")

# Upload da imagem
uploaded_file = st.file_uploader("Envie uma imagem do cartão de crédito", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.success("Imagem carregada com sucesso!")

    # Exibe a imagem enviada
    st.image(uploaded_file, caption="Imagem carregada", use_column_width=True)

    # Botão para processar a imagem
    if st.button("Validar Cartão"):
        try:
            connection_string = get_connection_string()

            # Faz upload da imagem para o Azure Blob
            blob_url = upload_image_to_blob(uploaded_file, connection_string)
            st.write("Imagem enviada para o Blob com sucesso!")

            # Envia a imagem para o modelo de IA
            validation_result = analyze_credit_card(blob_url)

            # Mostra os resultados
            show_image_and_validation(uploaded_file, validation_result)

        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
else:
    st.info("Por favor, envie uma imagem para continuar.")
