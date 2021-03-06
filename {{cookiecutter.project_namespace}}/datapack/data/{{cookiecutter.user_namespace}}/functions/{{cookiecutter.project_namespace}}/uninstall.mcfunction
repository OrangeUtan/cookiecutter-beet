# Unistall datapack
# Remove scoreboard objectives, teams, storage, etc here

tellraw @a[tag=!global.ignore,tag=!global.ignore.gui] ["",{"text":"Uninstalling ","color":"gold"},{"text":"{{cookiecutter.project_name}} ","color":"red"}, {"storage": "{{cookiecutter.user_namespace}}.{{cookiecutter.project_namespace}}", "nbt": "version", "color":"red"}]

# Remove advancements
advancement revoke @a from {{cookiecutter.user_namespace}}:{{cookiecutter.project_namespace}}:root

# Remove version
data remove storage minecraft:{{cookiecutter.user_namespace}}.{{cookiecutter.project_namespace}} version
