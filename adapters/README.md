# Adaptadores

Adaptadores traduzem workflows genéricos do PyGod para capacidades específicas de cada IDE.

## Contrato

Cada adaptador deve expor:

```text
detect
context
run <stage>
artifacts
```

Stages válidos:

- `discover`
- `spec`
- `plan`
- `implement`
- `verify`
- `finish`

## Registro

Toda IDE suportada deve constar em `supported_ides.json`.

## Regras

- Adaptadores não devem conter lógica de negócio do projeto.
- Adaptadores devem invocar scripts genéricos em `scripts/`.
- Saídas devem ser JSON.
- Segredos devem ser mascarados antes de persistir artefatos.
