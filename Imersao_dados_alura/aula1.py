import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# print(df.head(20))
# df.info()
# print(df.describe())
# print(df.shape)

# linhas, colunas = df.shape[0], df.shape[1]

# print(f'Linhas: {linhas}')
# print(f'Colunas: {colunas}')

# print(df.columns)

renomear_colunas = {
    'work_year':'ano',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia_emprego',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)
print(df.columns)

renomear_nivel_experiencia = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df["nivel_experiencia"] = df["nivel_experiencia"].replace(renomear_nivel_experiencia)
print(df["nivel_experiencia"].value_counts())

renomear_tipo_emprego = {
    'FT' : 'Integral',
    'CT': 'Parcial',
    'PT': 'Contrato',
    'FL': 'Freela'
}
df["tipo_emprego"] = df["tipo_emprego"].replace(renomear_tipo_emprego)
print(df["tipo_emprego"].value_counts())

renomear_taxa_remoto = {
    0 : 'Presencial',
    50 : 'Hibrido',
    100 : 'Remoto'
}

df["taxa_remoto"] = df['taxa_remoto'].replace(renomear_taxa_remoto)
print(df["taxa_remoto"].value_counts())
renomear_tamanho_empresa = {
    'M': 'Media',
    'L': 'Grande',
    'S': 'Pequena'
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(renomear_tamanho_empresa)
print(df["tamanho_empresa"].value_counts())


print(df.head())

print(df.describe(include="object"))
