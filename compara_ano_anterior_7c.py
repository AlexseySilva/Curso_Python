produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

import pandas as pd
lista = []

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        variacao = float((vendas2020[i]/vendas2019[i])-1)
        registros = [f'{produto}',f'{vendas2019[i]:_}'.replace('_','.'),f'{vendas2020[i]:_}'.replace('_','.'), f'{variacao:.3}']
        lista.append(registros)

df = pd.DataFrame(lista, columns=['Produto', 'Vendas 2019 (R$)', 'Vendas 2020 (R$)', 'Variação %'])
df['Variação %'] = df['Variação %'].apply(pd.to_numeric)
pd.options.display.float_format = '{:.2%}'.format
df = df.sort_values(by=['Variação %'])
df
