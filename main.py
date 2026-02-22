import streamlit as st

# Configuração da página - 100% de aproveitamento de tela
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para molduras redondas perfeitas e padronização
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    hr { margin: 1em 0; border: 0; border-top: 1px solid #ddd; }
    
    /* Moldura Redonda Padronizada */
    .img-circular {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #004A99;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    .container-equipe {
        text-align: center;
        margin-bottom: 20px;
    }

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
    # Para as coordenadoras também usaremos a moldura redonda
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular"><br><b>Irmã Olinda</b><br><small>Diretora</small></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular"><br><b>Ingrit Candido</b><br><small>Coord. Fund 2 e Integral</small></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular"><br><b>Josiane Dellaqua</b><br><small>Coord. Infantil e Fund 1</small></div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Corpo Docente - Ensino Fundamental 2")
    
    # Linha 1 de Professores com Moldura HTML
    cp1, cp2, cp3, cp4 = st.columns(4)
    with cp1:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/ana.jpg" class="img-circular"><br><b>Ana Desirée</b><br><small>Inglês</small></div>', unsafe_allow_html=True)
    with cp2:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/brendon.jpg" class="img-circular"><br><b>Brendon</b><br><small>Língua Portuguesa</small></div>', unsafe_allow_html=True)
    with cp3:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/evandro.jpg" class="img-circular"><br><b>Evandro</b><br><small>Educação Física</small></div>', unsafe_allow_html=True)
    with cp4:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/jose.jpg" class="img-circular"><br><b>José Pedro</b><br><small>Geografia</small></div>', unsafe_allow_html=True)

    # Linha 2 de Professores
    cp5, cp6, cp7, cp8 = st.columns(4)
    with cp5:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/leo.jpg" class="img-circular"><br><b>Leo</b><br><small>Matemática</small></div>', unsafe_allow_html=True)
    with cp6:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/luci.jpg" class="img-circular"><br><b>Luci</b><br><small>Ensino Religioso e Arte</small></div>', unsafe_allow_html=True)
    with cp7:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/maika.jpg" class="img-circular"><br><b>Maika</b><br><small>Filosofia</small></div>', unsafe_allow_html=True)
    with cp8:
        st.markdown('<div class="container-equipe"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/william.jpg" class="img-circular"><br><b>William</b><br><small>História</small></div>', unsafe_allow_html=True)

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Estar devidamente uniformizado e colocar nome em todas as peças. Não serão permitidas outras cores.")
        st.write("### 📚 Biblioteca e Literatura")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- **Multas por atraso:** Infantil e Fund I (por semana); Fund II (R$ 4,00 por dia).")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Duração média de 20 minutos, organizados a partir de março.")
        st.write("- **Infantil/Fund I:** Agendar via agenda conforme horários da escola.")
        st.write("- **Fund II:** Solicitar na Secretaria conforme disponibilidade.")

    with col_b:
        st.write("### 💊 Medicação e Saúde")
        st.write("Administração somente mediante receita médica e autorização assinada.")
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)")
        st.write("Educação Infantil e Fundamental I. Proibido eletrônicos ou bolas.")
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Tempo de lanche: 15 minutos; orientamos o envio de lanche saudável.")
        st.write("- Aniversários (Infantil/Fund I): Kits individuais com agendamento via agenda e Secretaria.")
        st.write("### 📝 Avisos Finais")
        st.write("- Acompanhar a lição de casa diariamente para incentivar a autonomia.")
        st.write("- Alterações cadastrais devem ser comunicadas via agenda.")

with tab4:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Período Manhã\n**07h25 às 12h10**\nFundamental I e II")
    with col_h2:
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)")
    st.warning("⚠️ **Tolerância:** 10 minutos. Após isso, o aluno ingressa apenas na 2ª aula.")
    st.write("Atrasos superiores exigem atestado médico ou justificativa dos responsáveis.")

with tab5:
    st.header("Sistema de Avaliação e Controle")
    st.write("### 📊 Ensino Fundamental (1º ao 9º ano)")
    st.write("- **Média Bimestral:** 6.0")
    st.write("- **Aprovação Final:** Média Final (MF) ≥ 24.0")
    st.latex(r'''\text{Média} = \frac{P1 (\text{Atividades Formativas}) + P2 (\text{Prova Bimestral})}{2}''')
    st.write("- **P1 (10,0):** Trabalhos, pesquisas, testes e atividades formativas.")
    st.write("- **P2 (10,0):** Prova bimestral.")
    st.write("---")
    st.write("### 💻 Sistema Notas Online (www.notasonline.com)")
    st.error("Registros incluem: desentendimento, desrespeito, dano material, atrasos e uniforme incompleto.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus e parques.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("- **Obrigatória autorização prévia dos pais**.")
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
    st.link_button("Abrir Formulário no Navegador", "https://docs.google.com/forms/d/e/SeuFormularioAqui")
