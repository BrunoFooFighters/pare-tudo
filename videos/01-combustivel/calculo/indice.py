import pandas as pd, unicodedata, re, sys
S='/tmp/claude-0/-home-user/5d75380e-a65a-5556-9bb4-6986bd67e44d/scratchpad/dl/'
def n(s):
    s=unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().upper()
    s=re.sub(r'[^A-Z]','',s)
    return AL.get(s,s)
AL={'SANTAIZABELDOPARA':'SANTAISABELDOPARA','AREZ':'ARES','MUNHOZDEMELO':'MUNHOZDEMELLO','BALNEARIODEPICARRAS':'BALNEARIOPICARRAS',
'PRESIDENTECASTELOBRANCO':'PRESIDENTECASTELLOBRANCO','SANTOANTONIODOLEVERGER':'SANTOANTONIODELEVERGER','LAGEADOGRANDE':'LAJEADOGRANDE'}
c=pd.read_csv('rm_mun.csv'); g=pd.read_csv('rms_pop.csv').head(50)
c=c[c.LABEL_CATMETROPOL.isin(g.LABEL_CATMETROPOL)].copy()
c['k']=c.SIGLA_UF+'|'+c.NOME_MUN.map(n)
# frota
f=pd.read_excel(S+'senatran/frota_set2026.xlsx',header=3)
f=f[f.UF.astype(str).str.len()==2]
excl=['REBOQUE','SEMI-REBOQUE','SIDE-CAR','BONDE']
f['VEIC']=f.TOTAL-f[excl].sum(axis=1)
f['k']=f.UF+'|'+f.MUNICIPIO.map(n)
fm=f.set_index('k')
# postos
r=pd.read_csv(S+'anp/revendedores.csv',sep=';',dtype=str)
r['k']=r.UF+'|'+r.MUNICIPIO.map(n)
pc=r.groupby('k').size()
# tancagem
t=pd.read_csv(S+'anp/tanc_out2026.csv',sep=';',encoding='latin1',thousands='.',decimal=',')
t.columns=['DATA','EMPRESA','UF','MUN','CNPJ','COD','SEG','DET','TAG','TIPO','GRUPO','M3']
t=t[t.SEG.isin(['TERMINAL','BASES DO RAMO DE COMBUSTÍVEIS','REFINARIA'])&(t.GRUPO=='DERIVADOS E BIOCOMBUSTÍVEIS')]
t['k']=t.UF+'|'+t.MUN.map(n)
tc=t.groupby('k').M3.sum()
miss=[k for k in c.k if k not in fm.index]; print('sem frota:',miss,file=sys.stderr)
missp=[k for k in c.k if k not in pc.index]; print('sem posto:',len(missp),missp[:15],file=sys.stderr)
mt=set(t.k)-set(pd.concat([pd.Series(list(fm.index))])); print('tanc nao casou:',list(mt)[:10],file=sys.stderr)
c['veic']=c.k.map(fm.VEIC).fillna(0); c['auto']=c.k.map(fm.AUTOMOVEL).fillna(0); c['moto']=c.k.map(fm.MOTOCICLETA+fm.MOTONETA).fillna(0)
c['postos']=c.k.map(pc).fillna(0); c['tanc']=c.k.map(tc).fillna(0)
a=c.groupby('LABEL_CATMETROPOL')[['POP','veic','auto','moto','postos','tanc']].sum()
# trilhos eletricos (km, ANPTrilhos 2025, IN-002-a)
km={'RM de São Paulo (SP)':273.2+89.7+14.5,'RM da Baixada Santista (SP)':19.5,'RM do Rio de Janeiro (RJ)':285.9,
 'RM de Porto Alegre (RS)':42.9,'RIDE do Distrito Federal e Entorno':42.4,'RM de Recife (PE)':37.7,'RM de Salvador (BA)':34.4,
 'RM de Belo Horizonte (MG)':28.1,'RM de Fortaleza (CE)':24.1}
a['km_elet']=a.index.map(km).fillna(0)
a['A_veic_1000']=a.veic/a.POP*1000
a['B_veic_posto']=a.veic/a.postos
a['C_km_milhao']=a.km_elet/a.POP*1e6
a['D_litros_veic']=a.tanc*1000/a.veic
# rank: 1 = mais vulnerável
a['rA']=a.A_veic_1000.rank(ascending=False,method='average')
a['rB']=a.B_veic_posto.rank(ascending=False,method='average')
a['rC']=a.C_km_milhao.rank(ascending=True,method='average')
a['rD']=a.D_litros_veic.rank(ascending=True,method='average')
a['media']=a[['rA','rB','rC','rD']].mean(axis=1)
a=a.sort_values(['media','B_veic_posto'],ascending=[True,False])
a['pos']=range(1,51)
a.to_csv('indice.csv')
pd.set_option('display.width',250)
print(a[['pos','POP','A_veic_1000','B_veic_posto','C_km_milhao','D_litros_veic','rA','rB','rC','rD','media']].round(1).to_string())
