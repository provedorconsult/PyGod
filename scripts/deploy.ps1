param(
    [string]$Target = $env:PYGOD_DEPLOY_TARGET,
    [string]$Command = $env:PYGOD_DEPLOY_COMMAND
)

if (-not $Target) {
    Write-Error "Deploy não configurado. Defina PYGOD_DEPLOY_TARGET ou passe -Target."
    exit 1
}

if (-not $Command) {
    Write-Error "Deploy não configurado. Defina PYGOD_DEPLOY_COMMAND ou passe -Command."
    exit 1
}

Write-Output "Deploy target: $Target"
Invoke-Expression $Command
