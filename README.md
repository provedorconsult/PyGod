# PyGod

Template universal de desenvolvimento para projetos com Python, Go, Docker, PostgreSQL e agentes de IA.

O repositório separa o núcleo reutilizável do projeto dos adaptadores específicos de IDE. A compatibilidade inicial mira Codex e Antigravity, mantendo espaço para Cursor, Windsurf e outras plataformas futuras.

## Estrutura

- `docs/`: PRD, SPEC, PLAN, REVIEW e modelos de governança.
- `services/`: código independente de IDE, separado por linguagem ou módulo.
- `db/`: migrações e seeds PostgreSQL.
- `.codex/`: workflows SpecPilot para agentes.
- `adapters/`: integrações por IDE.
- `scripts/`: automações genéricas de validação, build, testes e deploy.

## Uso rápido

1. Leia `docs/PRD.md`, `docs/SPEC.md` e `docs/PLAN.md`.
2. Execute a validação estrutural:

```powershell
python scripts/validate_template.py
```

3. Escolha um adaptador:

```powershell
python adapters/codex/adapter.py detect
python adapters/antigravity/adapter.py detect
python adapters/mock-ide/adapter.py detect
```

4. Execute um workflow genérico:

```powershell
python adapters/codex/adapter.py run discover
python adapters/antigravity/adapter.py run discover
```

## Adaptadores

Cada adaptador deve implementar as operações:

- `detect`: identifica disponibilidade e capacidades da IDE.
- `context`: lê estado do projeto, sprints e context capsules.
- `run <stage>`: traduz `discover`, `spec`, `plan`, `implement`, `verify` e `finish` para a IDE.
- `artifacts`: informa onde saídas e evidências são persistidas.

Consulte `adapters/README.md` para o contrato completo.
