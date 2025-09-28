import pandas as pd

# Ruta al archivo Excel
excel_path = r"C:\Users\s.travieso\OneDrive - UFV\Python\web_salario_convenio\data\categorias_precios.xlsx"

# Leer la hoja "categorías"
df = pd.read_excel(excel_path, sheet_name="categorías")

# Limpiar los nombres de columnas para evitar espacios extraños
df.columns = df.columns.str.strip()

# Guardar en JSON (orientación de registros → lista de objetos)
json_path = excel_path.replace(".xlsx", ".json")
df.to_json(json_path, orient="records", force_ascii=False, indent=2)

print(f"Archivo JSON creado en: {json_path}")
