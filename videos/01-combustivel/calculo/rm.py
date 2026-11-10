import pandas as pd, sys
D='/tmp/claude-0/-home-user/5d75380e-a65a-5556-9bb4-6986bd67e44d/scratchpad/dl/ibge/'
c=pd.read_excel(D+'Composicao_RM_2025_v2.xls',sheet_name=0)
p=pd.read_excel(D+'CD2022_Populacao_Coletada_Imputada_e_Total_Municipio_e_UF_20231222.xlsx',sheet_name=0,header=2).iloc[:,1:]
p['m']=pd.to_numeric(p['COD. MUNIC'],errors='coerce');p['u']=pd.to_numeric(p['COD. UF'],errors='coerce');p=p.dropna(subset=['m','u'])
p['COD_MUN']=(p.u*100000+p.m).astype(int)
p['POP']=pd.to_numeric(p['POP. TOTAL'],errors='coerce')
c=c[c.LABEL_CATMETROPOL.str.match(r'^(RM |RIDE|RAIDE)')]
# RM do Entorno do DF overlaps RIDE DF?
ride=set(c[c.LABEL_CATMETROPOL=='RIDE do Distrito Federal e Entorno'].COD_MUN)
ent=set(c[c.LABEL_CATMETROPOL=='RM do Entorno do Distrito Federal'].COD_MUN)
print('entorno in ride:',len(ent&ride),'/',len(ent),file=sys.stderr)
c=c[c.LABEL_CATMETROPOL!='RM do Entorno do Distrito Federal'].drop_duplicates(['LABEL_CATMETROPOL','COD_MUN'])
c=c[c.LABEL_CATMETROPOL!='RM do Norte/Nordeste Catarinense (SC)']
c=c[~((c.NOME_MUN=='TIMON')&(c.LABEL_CATMETROPOL!='RIDE da Grande Teresina (PI/MA)'))]
c=c[~((c.NOME_MUN=='LAGOA DA CONFUSÃO')&(c.LABEL_CATMETROPOL=='RM de Gurupi (TO)'))]
assert not c.COD_MUN.duplicated().any()
c=c.merge(p[['COD_MUN','POP']],on='COD_MUN',how='left')
print('missing pop', c.POP.isna().sum(),file=sys.stderr)
g=c.groupby('LABEL_CATMETROPOL').agg(pop=('POP','sum'),nmun=('COD_MUN','nunique')).sort_values('pop',ascending=False).reset_index()
g.to_csv('rms_pop.csv',index=False)
c.to_csv('rm_mun.csv',index=False)
print(g.head(55).to_string())
