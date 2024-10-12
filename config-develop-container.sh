#!/bin/bash

pip install -r /app/aplicacao-1/requirements.txt

pip install -r /app/aplicacao-2/requirements.txt

export DJANGO_SETTINGS_MODULE=teste_nimbus.settings

/bin/sleep infinity