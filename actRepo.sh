#!/bin/bash

# Asegurarse de estar en el directorio del repositorio
#cd /ruta/al/repo

# Definir usuario y contraseña
username="lucaschej"
password="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"

# Autenticación interactiva para git push
git add .
git commit -m "update"
git push https://$username:$password@github.com/lucaschej/2023.git master

