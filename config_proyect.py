import os

# Carpetas del proyecto
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/models",
    "src/utils",
    "results",
    "exports",
    "config"
]

# Crear carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Contenido del archivo config.yaml
config_yaml_content = """# Configuración del proyecto
paths:
  raw_data: data/raw
  processed_data: data/processed
  model_dir: src/models
  exports_dir: exports

train:
  test_size: 0.2
  random_state: 42
  batch_size: 32
  learning_rate: 0.001
  epochs: 10
"""


# Archivos a crear
files = {
    "README.md": "# Prueba Data Science\n",
    "requirements.yml": """name: test_ds_i4
channels:
  - defaults
  - conda-forge
  - pytorch
dependencies:
  - python=3.10
  - jupyterlab
  - matplotlib
  - pandas
  - numpy
  - scikit-learn
  - opencv
  - pip
""",
    "notebooks/0_exploracion_dataset.ipynb": "",
    "notebooks/1_entrenamiento_base.ipynb": "",
    "config/config.yaml": config_yaml_content
}

# Crear los archivos
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
