# PLAN - Implantação PyGod

## Fase 0 - Preparação

- Validar PRD e confirmar escopo: Go, Python, PostgreSQL, Codex, Antigravity e futuras IDEs.
- Definir papéis: gerente de projeto, arquiteto, desenvolvedores e responsáveis por IDE.
- Confirmar cronograma preliminar e critérios de aceite.

## Fase 1 - Estruturação do Repositório

- Criar diretórios `docs/`, `services/`, `db/`, `.codex/`, `adapters/` e `scripts/`.
- Publicar `PRD.md`, `SPEC.md`, `PLAN.md` e `REVIEW.md`.
- Definir convenções de commit e branches principais.

## Fase 2 - Núcleo Universal

- Criar layout de código para Go, Python e frontend.
- Criar scripts genéricos de validação, build, testes e deploy.
- Definir context capsules para tasks.
- Escrever workflows SpecPilot.

## Fase 3 - Adaptador Codex

- Implementar CLI mínima do adaptador.
- Definir `codex-config.yaml`.
- Traduzir stages genéricos para execução single-agent.
- Validar fluxo `discover -> finish`.

## Fase 4 - Adaptador Antigravity

- Implementar CLI mínima do adaptador.
- Definir `manager-config.json`.
- Mapear papéis manager, writer, critic e tester.
- Validar geração de artefatos para revisão humana.

## Fase 5 - Validação e Compatibilidade

- Executar a mesma SPEC via Codex e Antigravity.
- Comparar evidências e comportamento dos adaptadores.
- Ajustar núcleo quando houver dependência indevida de IDE.

## Fase 6 - Documentação e Treinamento

- Documentar inicialização de projeto.
- Documentar escolha e ativação de IDE.
- Preparar material de treinamento interno.

## Fase 7 - Suporte a Novas IDEs

- Manter adaptador `mock-ide` como referência.
- Definir homologação para novas IDEs.
- Revisar contrato de adaptadores a cada nova integração.

## Fase 8 - Lançamento e Iteração

- Lançar beta para equipes piloto.
- Coletar feedback.
- Monitorar mudanças de Codex e Antigravity.
- Atualizar roadmap de novas IDEs.

## Backlog Inicial

| ID | Item | Aceite |
| --- | --- | --- |
| feat-001 | Estrutura base do template | Diretórios, docs e validação estrutural criados |
| feat-002 | Adaptador Codex | CLI responde `detect`, `context`, `run` e `artifacts` |
| feat-003 | Adaptador Antigravity | CLI responde `detect`, `context`, `run` e `artifacts` |
| feat-004 | Adaptador mock | Exemplo extensível registrado em `supported_ides.json` |
| feat-005 | Evidências | `docs/REVIEW.md` recebe resultados de validação |
