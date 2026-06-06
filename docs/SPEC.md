# SPEC - PyGod

## 1. Arquitetura

PyGod é dividido em núcleo universal e adaptadores de IDE.

```text
docs/                 Governança e evidências
services/             Código de aplicação independente de IDE
db/                   Migrações e seeds PostgreSQL
.codex/workflows/     Fluxos SpecPilot
adapters/             Tradução de tarefas para cada IDE
scripts/              Automação genérica
```

## 2. Núcleo Universal

O núcleo define documentos, scripts e contratos compartilhados. Ele não deve depender de recursos exclusivos do Codex, Antigravity ou qualquer IDE futura.

### 2.1 Documentos

- `docs/PRD.md`: requisitos de produto.
- `docs/SPEC.md`: especificação técnica.
- `docs/PLAN.md`: fases, backlog e critérios.
- `docs/REVIEW.md`: evidências, testes e decisões.

### 2.2 Serviços

`services/` reserva espaço para módulos em múltiplas linguagens:

- `services/go/`
- `services/python/`
- `services/frontend/`

### 2.3 Banco

`db/` contém:

- `migrations/`: scripts versionados.
- `seeds/`: dados iniciais.

## 3. Contrato de Adaptadores

Cada adaptador deve expor uma CLI simples:

```text
python adapters/<ide>/adapter.py detect
python adapters/<ide>/adapter.py context
python adapters/<ide>/adapter.py run <stage>
python adapters/<ide>/adapter.py artifacts
```

### 3.1 Stages suportados

- `discover`
- `spec`
- `plan`
- `implement`
- `verify`
- `finish`

### 3.2 Saída esperada

As respostas devem ser JSON para permitir integração com outras ferramentas.

## 4. Codex

O adaptador Codex traduz stages genéricos em comandos e prompts compatíveis com execução single-agent via CLI. Ele deve priorizar:

- execução sequencial;
- uso de scripts genéricos do template;
- registro de evidências;
- seleção configurável de modelo e limites.

## 5. Antigravity

O adaptador Antigravity traduz stages genéricos em instruções para coordenação multi-agente. Ele deve priorizar:

- papéis `manager`, `writer`, `critic` e `tester`;
- artefatos de revisão humana;
- regras e guardrails;
- testes no navegador quando houver UI.

## 6. Novas IDEs

Novas IDEs devem ser registradas em `adapters/supported_ides.json` e implementar o contrato mínimo. O adaptador `mock-ide` serve como exemplo.

## 7. Context Capsules

Tasks devem declarar os arquivos e trechos autorizados para leitura. A cápsula mínima é:

```json
{
  "task_id": "feat-001",
  "files": ["docs/SPEC.md"],
  "sections": ["3. Contrato de Adaptadores"]
}
```

## 8. Segurança

- Não versionar `.env`, tokens ou chaves.
- Preferir `.env.example`.
- Adaptadores devem mascarar segredos em logs e artefatos.
