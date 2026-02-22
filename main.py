import streamlit as st
import urllib.parse

# Configuração da página - Sem reduções
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    
    .img-container {
        text-align: center;
        padding: 10px;
        margin-bottom: 20px;
    }
    
    .img-circular {
        border-radius: 50%;
        border: 4px solid #004A99;
        object-fit: cover;
        width: 150px;
        height: 150px;
        margin-bottom: 10px;
    }

    .nome-equipe { font-weight: bold; font-size: 1.1em; margin-bottom: 2px; color: #004A99; }
    .cargo-equipe { font-size: 0.85em; color: #555; line-height: 1.2; }
    
    hr { margin: 2em 0; border: 0; border-top: 1px solid #ddd; }
    
    .qr-container {
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #004A99;
    }
    </style>
    """, unsafe_allow_html=True)

# URL base CORRETA para arquivos no GitHub (Link Raw)
base_url = "https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/"

# Cabeçalho
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image(f"{base_url}logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas - Conteúdo 100% integral
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos", "❓ Dúvidas"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Mantenedora e Congregação")
    st.write("- **Associação das Irmãs Teatinas da Imaculada Conceição:** Fundada em 21/07/1973.")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583.")
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("### 🤝 Comunidade")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="img-container"><img src="{base_url}logo.jpg" class="img-circular"><div class="nome-equipe">Irmã Olinda</div><div class="cargo-equipe">Diretora</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="img-container"><img src="{base_url}Ingrit.jpg" class="img-circular"><div class="nome-equipe">Ingrit Candido</div><div class="cargo-equipe">Coordenadora Fundamental 2 e<br>Integral Manhã</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="img-container"><img src="{base_url}Josi.jpg" class="img-circular"><div class="nome-equipe">Josiane Dellaqua</div><div class="cargo-equipe">Coordenadora Ed. Infantil, <br>Fundamental 1 e Integral Tarde</div></div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Corpo Docente - Ensino Fundamental 2")
    
    # Configuração Individual de Carga (Garante que a foto apareça)
    row1_c1, row1_c2, row1_c3, row1_c4 = st.columns(4)
    with row1_c1:
        st.markdown(f'<div class="img-container"><img src="{base_url}AnaDesirée.jpeg" class="img-circular"><div class="nome-equipe">Ana Desirée</div><div class="cargo-equipe">Inglês</div></div>', unsafe_allow_html=True)
    with row1_c2:
        st.markdown(f'<div class="img-container"><img src="{base_url}Brendon.jpeg" class="img-circular"><div class="nome-equipe">Brendon</div><div class="cargo-equipe">Língua Portuguesa</div></div>', unsafe_allow_html=True)
    with row1_c3:
        st.markdown(f'<div class="img-container"><img src="{base_url}Evandro.jpeg" class="img-circular"><div class="nome-equipe">Evandro</div><div class="cargo-equipe">Educação Física</div></div>', unsafe_allow_html=True)
    with row1_c4:
        st.markdown(f'<div class="img-container"><img src="{base_url}JoséPedro.jpeg" class="img-circular"><div class="nome-equipe">José Pedro</div><div class="cargo-equipe">Geografia</div></div>', unsafe_allow_html=True)

    row2_c1, row2_c2, row2_c3, row2_c4 = st.columns(4)
    with row2_c1:
        st.markdown(f'<div class="img-container"><img src="{base_url}Leo.jpeg" class="img-circular"><div class="nome-equipe">Leo</div><div class="cargo-equipe">Matemática</div></div>', unsafe_allow_html=True)
    with row2_c2:
        st.markdown(f'<div class="img-container"><img src="{base_url}Luci.jpeg" class="img-circular"><div class="nome-equipe">Luci</div><div class="cargo-equipe">Ensino Religioso e Arte</div></div>', unsafe_allow_html=True)
    with row2_c3:
        st.markdown(f'<div class="img-container"><img src="{base_url}Maika.jpeg" class="img-circular"><div class="nome-equipe">Maika</div><div class="cargo-equipe">Filosofia</div></div>', unsafe_allow_html=True)
    with row2_c4:
        st.markdown(f'<div class="img-container"><img src="{base_url}William.jpeg" class="img-circular"><div class="nome-equipe">William</div><div class="cargo-equipe">História</div></div>', unsafe_allow_html=True)

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Não serão permitidas outras cores.")
        st.write("### 📚 Biblioteca e Literatura (Infantil e Fund 1)")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        st.write("- **Multas por atraso:** Infantil e Fund I (multa por semana); Fund II (R$ 4,00 por dia).")
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Duração média de 20 minutos, organizados a partir de março.")
        st.write("- **Infantil/Fund I:** Agendar via agenda com horários informados pela escola.")
        st.write("- **Fund II:** Solicitar na Secretaria conforme disponibilidade.")
        st.write("- *Não haverá agendamentos em semanas de avaliação.*")

    with col_b:
        st.write("### 💊 Medicação e Saúde")
        st.write("Administração somente com receita médica e autorização assinada.")
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)")
        st.write("Educação Infantil e Fundamental I. Proibido eletrônicos ou bolas.")
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Lanche: 15 minutos; orientamos opções saudáveis.")
        st.write("- Aniversários: Kits individuais com agendamento via agenda e Secretaria.")
        st.write("### 📝 Lição de Casa e Cadastro")
        st.write("- Acompanhar diariamente para incentivar autonomia e responsabilidade.")
        st.write("- Alterações de telefone/e-mail devem ser comunicadas via agenda.")

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
    st.latex(r'''\text{Média} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''')
    st.write("- **P1 (10,0):** Trabalhos, pesquisas, testes e atividades formativas.")
    st.write("- **P2 (10,0):** Prova bimestral.")
    st.write("---")
    st.write("### 💻 Sistema Notas Online (www.notasonline.com)")
    st.write("Acesso a: Calendários, boletim, lição de casa e registro de ocorrências.")
    st.error("Registros incluem: desentendimento, desrespeito, dano material, atrasos e uniforme incompleto.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus, parques e grutas.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("- **Obrigatória autorização prévia dos pais.**")
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho de 2026**.")

with tab7:
    st.header("Canal de Comunicação Direta")
    st.markdown(f"""
    <div class="qr-container">
        <h3>Acesse nosso Formulário de Dúvidas</h3>
        <p>Utilize o QR Code abaixo para registrar dúvidas ou sugestões para retorno posterior da escola.</p>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://reuniao-pais-2026.streamlit.app" width="200">
    </div>
    """, unsafe_allow_html=True)
