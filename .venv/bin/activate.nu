$env.VIRTUAL_ENV = $"($env.PWD)/.venv"
$env.PATH = ($env.PATH | prepend $"($env.VIRTUAL_ENV)/bin")
$env.VIRTUAL_ENV_PROMPT = "(.venv)"
