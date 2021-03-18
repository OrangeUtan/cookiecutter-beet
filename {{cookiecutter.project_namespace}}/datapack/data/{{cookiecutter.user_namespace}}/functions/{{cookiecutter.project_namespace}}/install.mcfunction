# Initial setup. Only run once when the datapack gets first added to a world
# Create scoreboard objectives, teams, etc here

# Set currently installe datapack version
data modify storage minecraft:{{cookiecutter.user_namespace}}.{{cookiecutter.project_namespace}} version set value "{{cookiecutter.version}}"