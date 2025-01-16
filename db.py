import os
import json
from PySide6.QtCore import QTimer

APPDATA = str(os.getenv('APPDATA'))
FOLDER = os.path.join(APPDATA, 'mtz autoclick')
CONFIG_FILE = os.path.join(FOLDER, 'config.json')

# TODO: Implementar pasta/caminho para salvar em linux
# TODO: Criar funções para salvar configs do teclado

class CpsConfigSave:
    def __init__(self, input_type):
        self.type = input_type if input_type in ['mouse', 'keyboard'] else None
        self.cps = None
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.save_config)

    def update_cps(self, value):
        self.cps = value
        self.timer.start(500)  # 0.5s de delay adicionado toda vez que mudar

    def save_config(self):
        if self.cps is not None:
            if self.type == 'mouse':
                _update_mouse_cps(self.cps)
            elif self.type == 'keyboard':
                ...
            self.cps = None

def setup_db():
    if os.path.exists(FOLDER) and os.path.exists(CONFIG_FILE):
        return
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    config = {
        "mouse": {
            "cps": 10,
            "bind": "",
            "side": "left"},
        "keyboard": {
            "cps": 15,
            "bind": "",
            "key": ""}
    }

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def get_config():
    if not os.path.exists(CONFIG_FILE):
        setup_db()

    try:
        with open(CONFIG_FILE, 'r') as config_file:
            return json.load(config_file)
    except json.JSONDecodeError:
        return {"mouse": {"cps": 11, "bind": "", "side": "left"}, "keyboard": {"cps": 11, "bind": "", "key": ""}}

def save_config(config):
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def _update_mouse_cps(value):
    if not os.path.exists(CONFIG_FILE):
        setup_db()

    config = get_config()
    config['mouse']['cps'] = int(value)
    save_config(config)

def update_mouse_bind(key):
    if not os.path.exists(CONFIG_FILE):
        setup_db()

    config = get_config()
    config['mouse']['bind'] = str(key).lower().strip()
    save_config(config)

def update_mouse_side(side):
    if not os.path.exists(CONFIG_FILE):
        setup_db()

    if side.lower().strip() not in ['left', 'right']:
        print('Error: Invalid side in update_mouse_side')
        return None

    config = get_config()
    config['mouse']['side'] = str(side).lower().strip()
    save_config(config)
