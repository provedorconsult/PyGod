# Estado Atual e Plano de Correcao

## Objetivos do projeto

PyGod deve entregar um template universal para desenvolvimento com agentes de IA, cobrindo:

- nucleo independente de IDE com documentacao, scripts, servicos e banco;
- adaptadores para Codex e Antigravity;
- contrato reutilizavel para IDEs futuras;
- validacao estrutural reproduzivel;
- evidencias em `docs/REVIEW.md`;
- caminho de implantacao configuravel.

## Estado atual

Concluido:

- Repositorio inicializado e publicado em `origin/main`.
- Documentos base criados em `docs/`.
- Workflows SpecPilot criados em `.codex/workflows/`.
- Adaptadores minimos criados para Codex, Antigravity e mock IDE.
- Validador estrutural criado em `scripts/validate_template.py`.
- Script de deploy parametrizado criado em `scripts/deploy.ps1`.

Lacunas corrigidas nesta etapa:

- Instrucoes de agente consolidadas em `AGENTS.md`.
- Arquivo `.env.example` adicionado para explicitar variaveis de implantacao.
- Estado e plano de correcao registrados neste documento.
- Validador ampliado para checar instrucoes, configuracao de deploy e documento de status.

Lacuna ainda externa ao repositorio:

- Deploy real depende da definicao de `PYGOD_DEPLOY_TARGET` e `PYGOD_DEPLOY_COMMAND`, ou de um provedor especifico como Dokploy, Easypanel ou GitHub Actions.

## Plano de correcao e implantacao

1. Validar estrutura atual com `python scripts/validate_template.py`.
2. Garantir que todos os artefatos minimos estejam versionados.
3. Registrar evidencias em `docs/REVIEW.md`.
4. Fazer commit em branch de trabalho.
5. Abrir PR contra `main`.
6. Fazer merge apos validacao green.
7. Executar deploy quando o alvo estiver configurado.

## Criterio de implantacao

O deploy e considerado configurado quando:

- `PYGOD_DEPLOY_TARGET` identifica o ambiente;
- `PYGOD_DEPLOY_COMMAND` contem o comando de implantacao;
- o comando conclui com exit code `0`;
- a evidencia e registrada em `docs/REVIEW.md`.
