import streamlit as st

# Configuração da página - 100% de aproveitamento de tela
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para identidade visual
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    hr { margin: 1em 0; border: 0; border-top: 1px solid #ddd; }
    .qr-container {
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #004A99;
    }
    </style>
    """, unsafe_allow_html=True)

# Título e Logo Superior
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    # Usando o arquivo local diretamente
    st.image("logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas com 100% do conteúdo original
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos", "❓ Dúvidas"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Mantenedora e Congregação")
    st.write("- **Associação das Irmãs Teatinas da Imaculada Conceição:** Fundada em 21/07/1973.")
    st.write("- **Congregação:** Fundada em Nápoles (Itália) em 1583 pela Madre Ursula Benincasa.")
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("logo.jpg", width=180, caption="Irmã Olinda - Diretora")
    with c2:
        st.image("Ingrit.jpg", width=180, caption="Ingrit Candido - Coord. Fund 2 e Integral")
    with c3:
        st.image("Josi.jpg", width=180, caption="Josiane Dellaqua - Coord. Infantil e Fund 1")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Corpo Docente - Ensino Fundamental 2")
    
    # Linha 1 de Professores (Carga direta do arquivo local)
    cp1, cp2, cp3, cp4 = st.columns(4)
    with cp1:
        st.image("ana.jpg", width=150)
        st.write("**Ana Desirée**")
        st.caption("Inglês")
    with cp2:
        st.image("brendon.jpg", width=150)
        st.write("**Brendon**")
        st.caption("Língua Portuguesa")
    with cp3:
        st.image("evandro.jpg", width=150)
        st.write("**Evandro**")
        st.caption("Educação Física")
    with cp4:
        st.image("jose.jpg", width=150)
        st.write("**José Pedro**")
        st.caption("Geografia")

    # Linha 2 de Professores
    cp5, cp6, cp7, cp8 = st.columns(4)
    with cp5:
        st.image("leo.jpg", width=150)
        st.write("**Leo**")
        st.caption("Matemática")
    with cp6:
        st.image("luci.jpg", width=150)
        st.write("**Luci**")
        st.caption("Ensino Religioso e Arte")
    with cp7:
        st.image("maika.jpg", width=150)
        st.write("**Maika**")
        st.caption("Filosofia")
    with cp8:
        st.image("william.jpg", width=150)
        st.write("**William**")
        st.caption("História")

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Não serão permitidas outras cores.")
        st.write("### 📚 Biblioteca e Literatura")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- **Multas por atraso:** Infantil e Fund I (por semana); Fund II (R$ 4,00 por dia).")
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Duração média de 20 minutos, organizados a partir de março.")
        st.write("- Agendar via agenda com antecedência de 24h a 48h.")

    with col_b:
        st.write("### 💊 Medicação e Saúde")
        st.write("Administração somente com receita médica e autorização assinada.")
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)")
        st.write("Educação Infantil e Fundamental I. Proibido eletrônicos ou bolas.")
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Lanche: 15 minutos; orientamos opções saudáveis.")
        st.write("- Aniversários: Kits individuais com agendamento via agenda.")

with tab4:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Período Manhã\n**07h25 às 12h10**\nFundamental I e II")
    with col_h2:
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)")
    st.warning("⚠️ **Tolerância:** 10 minutos. Após isso, o aluno ingressa apenas na 2ª aula.")

with tab5:
    st.header("Sistema de Avaliação e Controle")
    st.write("### 📊 Ensino Fundamental (1º ao 9º ano)")
    st.write("- **Média Bimestral:** 6.0")
    st.write("- **Aprovação Final:** Média Final (MF) ≥ 24.0")
    st.latex(r'''\text{Média} = \frac{P1 + P2}{2}''')
    st.error("Registros incluem: desentendimento, desrespeito, dano material, atrasos e uniforme incompleto.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus e parques.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho**.")

with tab7:
    st.header("Canal de Comunicação Direta")
    st.markdown("""
    <div class="qr-container">
        <h3>Acesse nosso Formulário de Dúvidas</h3>
        <p>Aponte a câmera do seu celular para o QR Code abaixo.</p>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://reuniao-pais-2026.streamlit.app" width="200">
    </div>
    """, unsafe_allow_html=True)
