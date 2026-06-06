param(
    [string]$Target = $env:PYGOD_DEPLOY_TARGET
)

if (-not $Target) {
    Write-Error "Deploy não configurado. Defina PYGOD_DEPLOY_TARGET ou passe -Target."
    exit 1
}

Write-Output "Deploy target: $Target"
