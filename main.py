import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares e design limpo
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
    </style>
    """, unsafe_allow_html=True)

# URL base do seu repositório para as imagens
base_url = "https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/"

# Cabeçalho
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image(f"{base_url}logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Mantenedora e Congregação")
    st.write("- **Associação das Irmãs Teatinas da Imaculada Conceição:** Fundada em 21/07/1973.")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583.")
    
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f'''<div class="img-container">
            <img src="{base_url}logo.jpg" class="img-circular">
            <div class="nome-equipe">Irmã Olinda</div>
            <div class="cargo-equipe">Diretora</div>
        </div>''', unsafe_allow_html=True)

    with c2:
        st.markdown(f'''<div class="img-container">
            <img src="{base_url}Ingrit.jpg" class="img-circular">
            <div class="nome-equipe">Ingrit Candido</div>
            <div class="cargo-equipe">Coordenadora Fundamental 2 e<br>Integral Manhã</div>
        </div>''', unsafe_allow_html=True)

    with c3:
        st.markdown(f'''<div class="img-container">
            <img src="{base_url}Josi.jpg" class="img-circular">
            <div class="nome-equipe">Josiane Dellaqua</div>
            <div class="cargo-equipe">Coordenadora Ed. Infantil, <br>Fundamental 1 e Integral Tarde</div>
        </div>''', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Corpo Docente - Ensino Fundamental 2")
    
    # Lista atualizada com os dados das imagens enviadas
    professores = [
        {"nome": "Brendon", "materia": "Língua Portuguesa", "foto": "Brendon. Língua Portuguesa.jpeg"},
        {"nome": "Leo", "materia": "Matemática", "foto": "Leo Matemática.jpeg"},
        {"nome": "William", "materia": "História", "foto": "William história.jpeg"},
        {"nome": "José Pedro", "materia": "Geografia", "foto": "José Pedro geografia.jpeg"},
        {"nome": "Ana Desirée", "materia": "Inglês", "foto": "Ana Desirée inglês.jpeg"},
        {"nome": "Luci", "materia": "Ensino Religioso e Arte", "foto": "Luci Ensino Religioso e Arte.jpeg"},
        {"nome": "Maika", "materia": "Filosofia", "foto": "Maika filosofia.jpeg"},
        {"nome": "Evandro", "materia": "Educação Física", "foto": "Evandro educação física.jpeg"}
    ]

    # Organização em colunas (4 por linha)
    cols = st.columns(4)
    for i, prof in enumerate(professores):
        with cols[i % 4]:
            # Criando a URL final codificada para evitar erros com espaços no nome do arquivo
            foto_url = base_url + prof['foto'].replace(" ", "%20")
            st.markdown(f'''<div class="img-container">
                <img src="{foto_url}" class="img-circular" onerror="this.src='https://via.placeholder.com/150/004A99/FFFFFF?text=Foto'">
                <div class="nome-equipe">{prof['nome']}</div>
                <div class="cargo-equipe">{prof['materia']}</div>
            </div>''', unsafe_allow_html=True)

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Não serão permitidas outras cores.")
        
        st.write("### 📚 Biblioteca e Literatura (Infantil e Fund 1)")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- **Atrasos:** Infantil e Fund I (multa por semana); Fund II (R$ 4,00 por dia).")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        
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
        st.write("Objetivo: incentivar o compartilhar e a convivência coletiva.")
        
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
    st.write("- Custos de transporte/ingressos informados previamente.")
    
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho**.")
