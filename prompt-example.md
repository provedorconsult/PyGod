# Prompt inicial para usar PyGod com um PRD

Use este prompt ao iniciar um novo projeto baseado no template PyGod.

```text
Você está em um repositório baseado no template PyGod. Use o PRD fornecido como fonte de verdade.

Objetivo:
Transformar o PRD em um projeto executável seguindo a estrutura PyGod.

Regras:
1. Leia primeiro AGENTS.md, docs/PRD.md, docs/SPEC.md, docs/PLAN.md e docs/REVIEW.md.
2. Atualize docs/SPEC.md com a arquitetura técnica derivada do PRD.
3. Atualize docs/PLAN.md com fases, backlog, critérios de aceite e comandos de validação.
4. Implemente usando a estrutura:
   - services/ para código
   - db/ para migrações/seeds
   - scripts/ para automações
   - adapters/ apenas para integrações de IDE
5. Registre evidências em docs/REVIEW.md.
6. Rode python scripts/validate_template.py e os testes do projeto.
7. Se tudo estiver green, faça commit, push e deploy quando houver alvo configurado.

Comece auditando o PRD, identificando requisitos funcionais, não funcionais, riscos, módulos e primeiro incremento implementável.
```

## Como usar

1. Copie o PRD para `docs/PRD.md` ou informe o caminho do arquivo PRD ao Codex.
2. Abra uma sessão Codex na raiz do repositório.
3. Envie o prompt acima.
4. Exija que as decisões e evidências sejam registradas em `docs/SPEC.md`, `docs/PLAN.md` e `docs/REVIEW.md`.
5. Ao final, valide com:

```powershell
python scripts/validate_template.py
```
