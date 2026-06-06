# PRD - Template Universal de Desenvolvimento com Codex e Antigravity

## 1. Visão Geral

O objetivo deste projeto é definir um template de repositório universal para projetos de software que utilizem agentes de inteligência artificial em diferentes IDEs. Inicialmente, o template deve ser compatível com OpenAI Codex e Google Antigravity, com uma estrutura modular que facilite a inclusão de outras IDEs no futuro.

O projeto abstrai tarefas, fluxos e regras de desenvolvimento de forma independente da IDE, fornecendo adaptadores específicos para cada ambiente.

## 2. Contexto

Codex e Antigravity têm filosofias diferentes. O Codex privilegia execução profunda, CLI, otimização e eficiência em fluxos single-agent. O Antigravity privilegia coordenação multi-agente, artefatos de revisão humana, regras e testes no navegador.

Essa diferença orienta a arquitetura: o núcleo do template deve ser comum, enquanto os adaptadores traduzem tarefas genéricas para as capacidades de cada IDE.

## 3. Problema e Oportunidade

Desenvolvedores precisam escolher entre IDEs de IA com formatos próprios de workflow, scripts e integrações. Isso gera fragmentação, retrabalho e risco de dependência de plataforma.

O template universal oferece:

- Padronização de artefatos como PRD, SPEC, PLAN, REVIEW e tasks.
- Flexibilidade para suportar múltiplas IDEs.
- Separação entre regras de negócio e integração com IDE.
- Reaproveitamento de práticas multi-agente e single-agent.

## 4. Objetivos

- Compatibilidade inicial com Codex e Antigravity.
- Núcleo universal com documentos, tasks, scripts e contratos genéricos.
- Adaptadores isolados em `adapters/`.
- Documentação padronizada e independente de IDE.
- Processo claro para inclusão de novas IDEs.

## 5. Requisitos Funcionais

### 5.1 Núcleo Universal

O template deve conter:

- `docs/`: `PRD.md`, `SPEC.md`, `PLAN.md`, `REVIEW.md` e templates.
- `services/`: módulos Go, Python e futuros serviços.
- `db/`: migrações e seeds.
- `.codex/`: workflows SpecPilot.
- `adapters/`: adaptadores para Codex, Antigravity e IDEs futuras.

### 5.2 Workflows

O template deve suportar:

- Fluxos multi-agente com checkpoints e artefatos de revisão.
- Fluxos single-agent sequenciais e otimizados.
- Etapas `discover`, `spec`, `plan`, `implement`, `verify` e `finish`.

### 5.3 Adaptadores

Cada adaptador deve implementar:

- Detectar ambiente e capacidades.
- Ler contexto, tasks e context capsules.
- Executar workflows.
- Persistir artefatos.
- Exibir checkpoints para aprovação humana.

### 5.4 Automação

O template deve fornecer scripts genéricos para validação estrutural, build, lint, testes e deploy. Adaptadores devem invocar esses scripts sem duplicar lógica.

## 6. Requisitos Não Funcionais

- Modularidade: adaptadores não podem quebrar o núcleo.
- Extensibilidade: novas linguagens, bancos e IDEs devem ser adicionáveis.
- Portabilidade: uso local e em nuvem, preferencialmente via contêineres.
- Usabilidade: documentação clara e comandos reproduzíveis.
- Segurança: segredos fora do repositório.
- Performance: workflows sem overhead desnecessário.

## 7. Restrições

- Antigravity depende de APIs e capacidades proprietárias.
- Codex depende de versões e modelos configuráveis.
- IDEs evoluem rapidamente; adaptadores devem ser fáceis de revisar.
- Integrações futuras podem exigir esforço específico por plataforma.

## 8. Critérios de Aceitação

- Projeto inicializado executa tarefas básicas via Codex e Antigravity.
- Adaptador mock demonstra extensibilidade para novas IDEs.
- `PRD`, `SPEC`, `PLAN`, `REVIEW` e `README` estão presentes.
- Fluxo `discover -> spec -> plan -> implement -> verify -> finish` está documentado.
- Scripts de qualidade e evidências de teste são registráveis em `docs/REVIEW.md`.
