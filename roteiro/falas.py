"""
roteiro/falas.py
----------------
Dados puros do roteiro. Nenhuma lógica aqui.

Cada item é uma tupla: (locutor, texto_com_ssml_opcional)
  - locutor: "jornalista" | "especialista"
  - texto: string com tags <break> do SSML onde necessário
"""

ROTEIRO: list[tuple[str, str]] = [
    ("jornalista", (
        "Você trabalha hoje numa empresa que desenvolve soluções de inteligência artificial "
        "com agentes embarcados para a indústria brasileira. Como você chegou até aqui?"
    )),
    ("especialista", (
        "Por acumulação de problemas, basicamente. "
        "Comecei lidando com dados desorganizados, aprendi a estruturá-los, "
        "depois precisei automatizar processos em cima dessa estrutura, "
        "e em algum momento percebi que a automação estava ficando inteligente o suficiente "
        "para tomar decisões simples sozinha. Foi aí que o mundo dos agentes entrou na minha vida. "
        "<break time='400ms'/>"
        "A indústria brasileira me fisgou porque é um setor que tem volumes absurdos de dado operacional "
        "e ainda processa boa parte disso de forma manual. "
        "Há um gap enorme entre o que a tecnologia já consegue fazer e o que as empresas industriais "
        "estão usando de fato. Trabalhar nesse gap é o que me move."
    )),
    ("jornalista", (
        "Explica para quem ainda confunde: qual a diferença real entre um chatbot tradicional "
        "e um sistema com agentes de inteligência artificial?"
    )),
    ("especialista", (
        "Chatbot tradicional é basicamente um mapa de decisões. "
        "Você pergunta X, ele responde Y. Se você sair do roteiro, ele trava ou te manda para um atendente humano. "
        "É uma árvore de fluxo com interface de conversa. "
        "<break time='400ms'/>"
        "Agente de IA é diferente em natureza. Ele não só responde, ele age. "
        "Pode consultar um banco de dados em tempo real, acionar um sistema externo, "
        "interpretar um documento, tomar uma sequência de decisões encadeadas com base no contexto. "
        "<break time='400ms'/>"
        "Na indústria isso faz diferença concreta. "
        "Um chatbot pode dizer: seu pedido está em processamento. "
        "Um agente pode verificar o estoque, cruzar com o calendário de produção, "
        "identificar um gargalo e já sugerir uma data alternativa de entrega, tudo dentro da mesma conversa. "
        "São produtos diferentes para problemas diferentes."
    )),
    ("jornalista", (
        "E o mercado industrial brasileiro entende essa diferença?"
    )),
    ("especialista", (
        "Entende cada vez mais, mas o caminho foi longo. "
        "Quando a gente chegava nas primeiras conversas com clientes, "
        "a maioria queria um chatbot que responde perguntas sobre o manual da máquina. Legítimo. "
        "<break time='400ms'/>"
        "Mas quando a gente começava a entender o processo deles de verdade, o problema real era outro: "
        "o técnico de manutenção passava horas tentando achar informação espalhada em três sistemas diferentes, "
        "o supervisor não sabia em tempo real o status de parada de equipamento, "
        "o time de compras tomava decisão com dado defasado. "
        "<break time='400ms'/>"
        "O chatbot que responde sobre manual era o sintoma. "
        "O problema era ausência de inteligência operacional acessível no momento certo. "
        "Quando você mostra isso para o cliente, a conversa muda de nível."
    )),
    ("jornalista", (
        "Esse reposicionamento do problema é um pivô? "
        "Como você reconhece quando é hora de mudar de direção?"
    )),
    ("especialista", (
        "É um pivô de diagnóstico, sim. "
        "E o sinal mais claro de que é hora de mudar é quando a solução que você está entregando "
        "resolve o problema declarado mas não muda nada de fato na operação do cliente. "
        "<break time='400ms'/>"
        "Já entregamos sistemas que funcionavam tecnicamente: "
        "o agente respondia, integrava, operava bem, "
        "e três meses depois o cliente usava pouco. "
        "Quando você vai investigar, descobre que o problema que ele verbalizou na venda "
        "não era o problema que travava o dia a dia dele. A dor real estava em outro lugar. "
        "<break time='400ms'/>"
        "Isso nos ensinou a fazer discovery mais profundo antes de qualquer proposta. "
        "Às vezes o cliente quer falar de tecnologia e você precisa insistir em falar de processo. "
        "Não é sempre confortável, mas é necessário."
    )),
    ("jornalista", (
        "Como é o processo de validação de uma solução antes de desenvolver tudo?"
    )),
    ("especialista", (
        "A gente chama internamente de semana de dor. "
        "Antes de qualquer linha de código, a gente passa tempo dentro da operação do cliente. "
        "Observa, conversa com operadores, supervisores, analistas. "
        "Não com o gestor que aprovou o projeto: com quem vai usar o sistema todo dia. "
        "<break time='400ms'/>"
        "Depois disso, mapeamos as três hipóteses mais fortes de onde o agente pode gerar impacto real. "
        "Construímos um protótipo funcional, mínimo mesmo, "
        "e testamos com um grupo pequeno de usuários reais. "
        "<break time='400ms'/>"
        "Se nesse teste a pessoa usa o agente de forma espontânea, sem precisar ser lembrada, é sinal positivo. "
        "Se ela usa só quando pedimos para usar, "
        "temos um problema de relevância que tecnologia nenhuma resolve depois."
    )),
    ("jornalista", (
        "Quais são os maiores desafios técnicos de levar agentes de IA "
        "para dentro de uma empresa industrial?"
    )),
    ("especialista", (
        "Três principais. "
        "O primeiro é dado. "
        "Dado industrial costuma ser fragmentado, inconsistente, "
        "armazenado em sistemas legados que não conversam entre si. "
        "Antes de construir qualquer agente inteligente, você precisa ter clareza "
        "sobre o que está disponível, onde está, e em que qualidade. "
        "Agente de IA sobre dado ruim produz resposta ruim com muita confiança. "
        "É pior do que não ter sistema. "
        "<break time='400ms'/>"
        "O segundo é integração. "
        "Indústria usa ERP, MES, SCADA, sistemas de gestão de manutenção, às vezes planilhas ainda. "
        "Fazer o agente conversar com tudo isso de forma confiável "
        "exige trabalho de engenharia que não aparece na apresentação de vendas "
        "mas domina a execução do projeto. "
        "<break time='400ms'/>"
        "O terceiro é latência de confiança. "
        "O operador de chão de fábrica não vai confiar num agente de IA na primeira semana. Nem na segunda. "
        "Você precisa construir uma história de acertos, "
        "começar por perguntas onde a resposta é verificável, "
        "onde o usuário consegue confirmar que o agente está certo. "
        "Confiança operacional se constrói devagar e quebra rápido."
    )),
    ("jornalista", (
        "E os desafios que não são técnicos?"
    )),
    ("especialista", (
        "São os mais difíceis. O principal é política interna. "
        "Quando você chega numa empresa industrial com uma solução "
        "que automatiza parte do trabalho de alguém, há resistência. "
        "Às vezes explícita, às vezes velada: "
        "alguém que esquece de cadastrar os dados corretamente, "
        "alguém que não repassa o acesso necessário, "
        "alguém que reporta para o gestor que o sistema não funciona "
        "quando na verdade nunca usou direito. "
        "<break time='400ms'/>"
        "Aprendemos que o projeto de IA precisa ter um sponsor interno "
        "com poder real e comprometimento genuíno. "
        "Não um gestor que aprovou no orçamento e esqueceu. "
        "Alguém que vai cobrar adoção, que vai comunicar para a equipe por que aquilo importa, "
        "que vai lidar com a resistência quando ela aparecer. "
        "Sem isso, a tecnologia mais sofisticada encalha."
    )),
    ("jornalista", (
        "Fale sobre um erro que a empresa cometeu e o que mudou depois."
    )),
    ("especialista", (
        "Já entregamos um agente com capacidades demais para o momento do cliente. "
        "Ele conseguia fazer consultas complexas, cruzar múltiplas bases, gerar relatórios analíticos. "
        "O cliente ficou impressionado na demonstração. "
        "No uso real, as pessoas pediam coisas simples e ficavam confusas com a profundidade das respostas. "
        "<break time='400ms'/>"
        "O erro foi não calibrar o agente para o nível de maturidade digital daquele usuário específico. "
        "A sofisticação que é virtude num contexto vira ruído em outro. "
        "<break time='400ms'/>"
        "Depois disso, a gente passou a construir perfis de usuário "
        "antes de definir as capacidades do agente. "
        "Quem vai usar, com que frequência, com que tipo de dado "
        "e para tomar que tipo de decisão. "
        "Isso define o que o agente precisa fazer, não o que ele é capaz de fazer."
    )),
    ("jornalista", (
        "Como vocês gerenciam projetos com recursos limitados, "
        "considerando que muitos clientes industriais têm orçamentos apertados para inovação?"
    )),
    ("especialista", (
        "Partimos do menor escopo que ainda gera resultado visível. "
        "Não o projeto completo: "
        "o primeiro caso de uso que a gente consegue entregar em seis a oito semanas "
        "e que o cliente consegue medir. "
        "Se o resultado aparecer, o orçamento para a próxima fase "
        "fica mais fácil de justificar internamente. "
        "<break time='400ms'/>"
        "Isso também nos protege. "
        "Projeto de IA com escopo aberto e prazo longo em ambiente industrial é receita para problema. "
        "As variáveis mudam, a prioridade do cliente muda, o contexto muda. "
        "Entregar valor em ciclos curtos mantém o projeto vivo e a confiança do cliente intacta."
    )),
]

