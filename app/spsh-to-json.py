import pygsheets
import numpy as np
import os
import json
import spreadsheet_maker

id_template = '1lRQKIO_z2k_EGt9f_VcTmKIaU2baXdniNPoN7tRo0Y0'

with open("default-template-spsh.json", 'w', encoding='utf-8') as f:
    json.dump(spreadsheet_maker.get_client().open_as_json(id_template), f, ensure_ascii=False, indent=4)
f.close()
