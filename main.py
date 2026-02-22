import streamlit as st

# Configuração da página - Foco em Professionalismo e Conteúdo Integral
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para identidade visual e fotos circulares
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    hr { margin: 1.5em 0; border: 0; border-top: 1px solid #ddd; }
    .qr-container {
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #004A99;
    }
    </style>
    """, unsafe_allow_html=True)

# URL base CORRETA para carregamento de imagens no GitHub (Link Raw)
base_url = "https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/"

# Cabeçalho Principal
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image(f"{base_url}logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas com 100% de Fidelidade ao Documento
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos", "❓ Dúvidas"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Mantenedora e Congregação")
    st.write("- **Associação das Irmãs Teatinas da Imaculada Conceição**: Fundada em 21/07/1973.")
    st.write("- **Congregação**: Fundada em Nápoles (Itália) em 1583 pela Madre Ursula Benincasa.")
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Estes são princípios a serem seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image(f"{base_url}logo.jpg", width=180)
        st.write("**Irmã Olinda**")
        st.caption("Diretora")
    with c2:
        st.image(f"{base_url}Ingrit.jpg", width=180)
        st.write("**Ingrit Candido**")
        st.caption("Coordenadora Fundamental 2 e Integral Manhã")
    with c3:
        st.image(f"{base_url}Josi.jpg", width=180)
        st.write("**Josiane Dellaqua**")
        st.caption("Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Corpo Docente - Ensino Fundamental 2")
    
    # Grid de Professores com links diretos corrigidos (.jpg conforme sua ação de renomear)
    cp1, cp2, cp3, cp4 = st.columns(4)
    with cp1:
        st.image(f"{base_url}ana.jpg", width=150)
        st.write("**Ana Desirée**")
        st.caption("Inglês")
    with cp2:
        st.image(f"{base_url}brendon.jpg", width=150)
        st.write("**Brendon**")
        st.caption("Língua Portuguesa")
    with cp3:
        st.image(f"{base_url}evandro.jpg", width=150)
        st.write("**Evandro**")
        st.caption("Educação Física")
    with cp4:
        st.image(f"{base_url}jose.jpg", width=150)
        st.write("**José Pedro**")
        st.caption("Geografia")

    cp5, cp6, cp7, cp8 = st.columns(4)
    with cp5:
        st.image(f"{base_url}leo.jpg", width=150)
        st.write("**Leo**")
        st.caption("Matemática")
    with cp6:
        st.image(f"{base_url}luci.jpg", width=150)
        st.write("**Luci**")
        st.caption("Ensino Religioso e Arte")
    with cp7:
        st.image(f"{base_url}maika.jpg", width=150)
        st.write("**Maika**")
        st.caption("Filosofia")
    with cp8:
        st.image(f"{base_url}william.jpg", width=150)
        st.write("**William**")
        st.caption("História")

with tab3:
    st.header("Orientações Educacionais e Avisos Gerais")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Estar devidamente uniformizado e colocar nome em todas as peças. Não serão permitidas outras cores.")
        st.write("### 📚 Biblioteca e Literatura")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        st.write("- **Multas por atraso**: Infantil e Fund I (por semana); Fund II (R$ 4,00 por dia).")
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Início em março; duração média de 20 minutos.")
        st.write("- **Infantil/Fund I**: Agendar via agenda conforme horários da escola.")
        st.write("- **Fund II**: Solicitar na Secretaria conforme disponibilidade.")

    with col_b:
        st.write("### 💊 Medicação e Saúde")
        st.write("Administração somente mediante receita médica e autorização assinada.")
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)")
        st.write("Educação Infantil e Fundamental I. Proibido eletrônicos ou bolas.")
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Tempo de lanche: 15 minutos; orientamos o envio de lanche saudável.")
        st.write("- Aniversários (Infantil/Fund I): Kits individuais agendados via secretaria.")
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
    st.warning("⚠️ **Tolerância**: 10 minutos para atrasos. Após isso, o aluno ingressa apenas na 2ª aula.")
    st.write("Atrasos superiores exigem atestado médico ou justificativa dos responsáveis.")

with tab5:
    st.header("Sistema de Avaliação e Controle")
    st.write("### 📊 Ensino Fundamental (1º ao 9º ano)")
    st.write("- **Média Bimestral**: 6.0")
    st.write("- **Aprovação Final**: Média Final (MF) igual ou superior a 24.0.")
    st.latex(r'''\text{Média} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''')
    st.write("---")
    st.write("### 💻 Sistema Notas Online")
    st.write("Acompanhe em: **www.notasonline.com**.")
    st.error("Registros incluem: desentendimento, desrespeito, dano material, atrasos e uniforme incompleto.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus, parques e grutas.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("- **Obrigatória autorização prévia dos pais**.")
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Atendimento focado na inclusão. Previsão de inauguração: **Julho de 2026**.")

with tab7:
    st.header("Canal de Comunicação Direta")
    st.markdown(f"""
    <div class="qr-container">
        <h3>Acesse nosso Formulário de Dúvidas</h3>
        <p>Utilize o QR Code abaixo para registrar dúvidas ou sugestões para retorno posterior da escola.</p>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://reuniao-pais-2026.streamlit.app" width="200">
    </div>
    """, unsafe_allow_html=True)
