import streamlit as st

# Configuração da página - 100% de aproveitamento de tela
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para identidade visual e Molduras Redondas Padronizadas
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    hr { margin: 1em 0; border: 0; border-top: 1px solid #ddd; }
    
    /* Estilo para fotos redondas e padronizadas */
    .img-circular {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #004A99;
        margin-bottom: 10px;
    }
    .equipe-container {
        text-align: center;
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

# Abas com 100% do conteúdo original (Sem resumos)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "☀️ Integral", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos", "❓ Dúvidas"
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
    
    # Linha 1 de Professores
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

    # Linha 3 de Professores
    cp9, cp10, cp11, cp12 = st.columns(4)
    with cp9:
        st.image("Edson.jpg", width=150)
        st.write("**Edson**")
        st.caption("Ciências")
    with cp10:
        st.image("Fernanda.jpg", width=150)
        st.write("**Fernanda**")
        st.caption("Educação Digital e LIV")

with tab3:
    st.header("Informativo do Integral - manhã")
    st.write("**Curitiba, 23 de fevereiro de 2026**")
    st.write("Prezadas famílias e queridos alunos,")
    st.write("Pensando sempre no aprendizado, no desenvolvimento integral e na qualidade de ensino, reformulamos as aulas do Integral para tornar a rotina ainda mais rica, dinâmica e significativa para nossos estudantes[cite: 1, 4].")
    st.write("A partir deste período, nossa grade de horários foi reorganizada, contemplando atividades diversificadas que estimulam o desenvolvimento cognitivo, social, emocional e criativo dos alunos. Convidamos todos a conferirem as novas grades de horário e as aulas disponíveis em cada ciclo[cite: 1, 5, 6].")
    st.write("Confira as novidades do Integral[cite: 1, 7]:")
    
    st.write("### 🧪 Atividades e Oficinas")
    st.write("- **Experiência / Pequenos Cientistas**: No laboratório de Ciências, as crianças vivenciam experiências práticas e seguras, explorando fenômenos como misturas, reações simples, estados físicos da matéria, plantio e observação da natureza. De forma lúdica, aprendem a observar, levantar hipóteses e registrar descobertas, despertando a curiosidade científica desde cedo[cite: 1, 8, 9].")
    st.write("- **Produção Textual (4º e 5º ano)**: Espaço dedicado ao desenvolvimento da escrita criativa e formal, trabalhando diferentes gêneros textuais, ampliação de vocabulário, organização de ideias e aprimoramento da expressão escrita[cite: 1, 10].")
    st.write("- **Contação de Histórias**: Momento de imaginação e encantamento, estimulando a escuta atenta, a interpretação e o gosto pela leitura[cite: 1, 11].")
    st.write("- **Iniciação Teatral**: Atividades que desenvolvem expressão corporal, oralidade, criatividade, autoconfiança e trabalho em grupo por meio de jogos e práticas teatrais[cite: 1, 12].")
    st.write("- **Oficina Criativa**: Exploração artística com diferentes materiais e técnicas, incentivando a criatividade, coordenação motora e expressão individual[cite: 1, 13].")
    st.write("- **Xadrez**: Desenvolvimento da concentração, planejamento, paciência e tomada de decisões estratégicas[cite: 1, 14].")
    st.write("- **Projeto**: Momento destinado a pesquisas, desenvolvimento de trabalhos interdisciplinares e aprofundamento de conteúdos[cite: 1, 15].")
    st.write("- **Culinária (quinzenal)**: Atividade prática que trabalha medidas, organização, autonomia, alimentação saudável e cooperação, além de proporcionar experiências sensoriais[cite: 1, 16].")
    st.write("- **Musicalização**: Vivências com ritmo, canto, percepção sonora e expressão musical, contribuindo para o desenvolvimento cognitivo e sensível[cite: 1, 17].")
    st.write("- **Raciocínio Lógico e Estratégia (2º ao 5º ano)**: Desafios, jogos e situações-problema que estimulam o pensamento lógico, a resolução de problemas e a tomada de decisões[cite: 1, 18].")
    st.write("- **Horta**: Contato direto com a natureza, plantio, cuidados com a terra e aprendizagem sobre sustentabilidade e alimentação saudável[cite: 1, 19].")
    st.write("- **Esportes**: Atividades que promovem coordenação motora, trabalho em equipe, respeito às regras e hábitos saudáveis[cite: 1, 20].")
    
    st.write("---")
    st.write("Além das aulas, os alunos continuam contando com momentos de descontração, café, descanso e almoço, garantindo equilíbrio entre aprendizagem e bem-estar[cite: 1, 21].")
    st.write("Estamos muito animados com essa nova organização e confiantes de que ela proporcionará experiências ainda mais significativas para nossos alunos[cite: 1, 22].")
    st.write("Contamos com a parceria de sempre! [cite: 1, 23]")
    st.write("**Com carinho, Equipe do Integral** [cite: 1, 24]")

with tab4:
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

with tab5:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Período Manhã\n**07h25 às 12h10**\nFundamental I e II")
    with col_h2:
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)")
    st.warning("⚠️ **Tolerância:** 10 minutos. Após isso, o aluno ingressa apenas na 2ª aula.")
    st.write("Atrasos superiores exigem atestado médico ou justificativa dos responsáveis.")

with tab6:
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

with tab7:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus e parques.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("- **Obrigatória autorização prévia dos pais**.")
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho**.")

with tab8:
    st.header("Canal de Comunicação Direta")
    st.markdown("""
    <div class="qr-container">
        <h3>Acesse nosso Formulário de Dúvidas</h3>
        <p>Aponte a câmera do seu celular para o QR Code abaixo.</p>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://reuniao-pais-2026.streamlit.app" width="200">
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir Formulário no Navegador", "https://docs.google.com/forms/d/e/SeuFormularioOriginalAqui")
