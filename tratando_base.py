import pandas as pd
import numpy as np

#======================================================================================#

def substituir_valores(df, coluna, sub1, sub2, regex):
    df[coluna] = df[coluna].astype(str).str.replace(sub1, sub2, regex=regex)

def deixando_maiusculo(df, coluna):
    df[coluna] = df[coluna].apply(lambda x: x.title() if pd.notnull(x) else x)

def numeros_negativos(df, coluna):
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    df.loc[df[coluna] < 0, coluna] = np.nan

def valores_com_intervalo(df, coluna, num1, num2):
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    df.loc[(df[coluna] < num1) | (df[coluna] > num2), coluna] = np.nan       

#======================================================================================#

def limpando_ticket_id(df, coluna="ticket_id"):
    df[coluna] = df[coluna].str.upper()
    substituir_valores(df, coluna, "TK-", "TCK-", False)

def limpando_created_at(df, coluna="created_at"):
    df[coluna] = df[coluna].astype(str).str.strip()
    df[coluna] = pd.to_datetime(df[coluna], format="%Y-%m-%d %H:%M:%S", errors="coerce")

def removendo_arroba(df):
    colunas = df.select_dtypes(include=["object", "str"]).columns.tolist()

    if "email" in colunas:
        colunas.remove("email")

    for coluna in colunas:
        substituir_valores(df, coluna, "@", "a", False)

def substituicao_geral(df):
    region = {
        "^wes.*": "west",
        "^eas.*": "east",
        "^cen.*": "central",
        "^sou.*": "south",
        "^nor.*": "north"
    }
    
    channel = {
        "^emai.*": "email",
        "^phon.*": "phone",
        "^social.*" : "social media",
        "^what.*": "whatsapp" 
    }
    
    product = {
        "^basic.*": "basic plan",
        "^deli.*": "delivery service",
        "^hardw.*": "hardware",
        "^market.*": "marketplace", 
        "^premi.*": "premium plan",
        "^subsc.*": "subscription",
        "^suppor.*": "support plan",
        "^web.*": "website"
    }

    issue_type = {
        "^account.*": "account suspension",
        "^billin.*": "billing",
        "^cancellatio.*": "cancellation",
        "^complain.*": "complaint",
        "^delivery.*": "delivery delay",
        "^login.*": "login issue",
        "^order.*": "order status",
        "^othe.*": "other",
        "^password.*": "password reset",
        "^product.*": "product defect",
        "^refun.*": "refund",
        "^subscriptio.*": "subscription",
        "^technical.*": "technical support",
        "^warranty.*": "warranty claim"
    }

    priority = {
        "^cri.*": "critical",
        "^h.*": "high",
        "^med.*": "medium",
        "^lo.*": "low"
    }

    status = {
        "^clos.*": "closed",
        "^esca.*": "escalated",
        "^in.*": "in progress",
        "^ope.*": "open",
        "^reso.*": "resolved"
    }

    sentiment = {
        "^nega.*": "negative",
        "^neu.*": "neutral",
        "^pos.*": "positive"
    }

    mapa_geral = {
        "region": region,
        "channel": channel,
        "product": product,
        "issue_type": issue_type,
        "priority": priority,
        "status": status,
        "sentiment": sentiment 
    }

    df.replace(mapa_geral, regex=True, inplace=True)

    df["order_amount_usd"] = df["order_amount_usd"].astype(str).str.replace("$", "", regex=False)

def limpando_customer_age(df, coluna="customer_age"):
    df[coluna] = df[coluna].astype(str).str.replace("twenty", "20", regex=False)
    valores_com_intervalo(df, coluna, 18, 100)

def corrigir_estado_cidade(df, col1="city", col2="state"):
    estado_na_col_cidade = df[col1].str.len() == 2
    cidade_na_col_estado = (df[col2].str.len() != 2) & df[col2].notna()
    filtro = estado_na_col_cidade | cidade_na_col_estado

    df.loc[filtro, [col1, col2]] = df.loc[filtro, [col2, col1]].values
     
    df[col2] = df[col2].apply(lambda x: x.upper() if pd.notnull(x) else x)
    deixando_maiusculo(df, col1)

#======================================================================================#

def limpeza_colunas(df):
    limpando_ticket_id(df)
    limpando_created_at(df)
    substituir_valores(df, "customer_id", "ID-", "", False)
    deixando_maiusculo(df, "customer_name")
    removendo_arroba(df)
    substituicao_geral(df)    
    deixando_maiusculo(df, "assigned_agent")
    limpando_customer_age(df)
    numeros_negativos(df, "first_response_min")
    valores_com_intervalo(df, "satisfaction_score", 0, 10)
    numeros_negativos(df, "resolution_hours")
    corrigir_estado_cidade(df)

def notificar_limpeza(lin_inicial, duplicadas, linhas_com_nulos, celulas_vazias, lin_final):
    relatorio = pd.DataFrame({
        "Métrica": [
            "Registros iniciais",
            "Duplicatas encontradas",
            "Linhas com valores ausentes",
            "Células vazias",
            "Registros finais"
        ],
        "Valor": [
            lin_inicial,
            duplicadas,
            linhas_com_nulos,
            celulas_vazias,
            lin_final
        ]
})

    print(relatorio)

#======================================================================================#

df = pd.read_csv("Base_de_Dados.csv")

lin_inicial = len(df)
duplicadas = df.duplicated().sum()

df = df.drop_duplicates()
df = df.map(lambda x: x.strip().lower() if isinstance(x, str) else x)
df = df.replace(["n/a", "unknown","unknow" ," ", "_", "-", "", "none"], np.nan)
limpeza_colunas(df)
df = df.convert_dtypes()

linhas_com_nulos = df.isna().any(axis=1).sum()
celulas_vazias = df.isna().sum().sum()
lin_final = len(df) 

notificar_limpeza(lin_inicial, duplicadas, linhas_com_nulos, celulas_vazias, lin_final)

df.to_csv("Base_de_Dados_tratada.csv", index=False)