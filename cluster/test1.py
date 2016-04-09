#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121)

## the data
N=1000
#x = np.random.randn(N)
#y = np.random.randn(N)

x=[59.5618738052369,13.805977554948868,10.372555473671552,34.41078374940049,83.55148974851187,42.95770314688859,29.344951567343557,75.86463035627236,30.269169261855712,63.36248625738019,89.9332101992005,12.818048844619835,91.21895157681001,17.0754009552915,63.61065039327395,46.20700132446564,8.961183979621401,65.96578222878257,71.65141806099956,17.123031363876716,36.50723755799682,35.72417305196593,45.4797236908733,26.731504267928084,82.44402511847206,85.3827644649281,68.69713909993422,29.906276379595496,30.17343011599688,74.2282910929206,61.689349474537636,54.44621602742388,93.20356739570403,55.430714819678784,45.212468541504236,40.37822739821368,9.643449111220725,54.736619449324564,79.9254302958883,62.20142293278547,2.6250919993587973,3.9079808884257994,10.129369063627092,54.54937020386655,98.59131396459372,4.639205380416445,40.56344520703513,89.09596014505185,16.023146694545687,29.317945939545687,53.72226361678748,58.429589317131935,74.98536109229359,9.467742168169535,69.55041595696045,80.33340122487296,75.77925812311481,20.464984676210165,32.29636707887358,92.44579812522025,85.45637234413529,34.66593526353081,40.44661789737728,54.988864217909104,56.565913227331876,80.5865193519142,59.55947972632435,70.0718206207311,86.79062680670316,98.63858976553819,0.316292205099844,73.86506130046756,72.5699844204588,61.89367598479395,5.525828892168727,51.127441304747265,19.726579465103246,69.76670315526789,98.87201270805444,2.3328532940010693,72.90766861824345,7.151161463167332,65.09188899669637,25.140349012061513,35.50905846151543,60.815808678074745,8.974073050696207,50.65862943575259,92.02822630023537,57.064620017031764,52.161195151914995,39.39762489795744,87.6983300276693,61.42193725490331,53.66664653223037,83.1455273633188,60.61583811446754,28.181444845857527,67.63226679253562,66.81790293975502]
y = [50.2319684393999,87.80096609962862,26.82600772086239,1.4690031204784848,58.17475970388468,43.040047202094,46.774541717163984,82.83803969786638,98.87829010913201,77.61484601325424,19.478526602240375,18.39847142671731,93.7477429797169,79.61828111025862,94.56479175118317,17.432621713681407,1.8976649391648004,7.81546605981156,93.98156448276872,90.9393463528562,71.37490984116693,78.28581613405733,6.115415445488692,50.243648767843275,38.79015871601329,60.72651611960189,83.03853676710492,10.439856668983104,58.209652974070224,38.24944946761536,39.354228645283825,30.310291834067492,96.0097963133815,35.765822424638195,86.99683220730643,77.15157384600548,5.097476593698158,85.33089837883944,54.94759591829165,35.28914008450573,63.06431820609561,40.343986210664376,58.99645846701809,50.235823241845765,99.58788912328419,26.73073499451005,40.677651601077756,81.30086211778598,46.67087752648258,86.0167792013545,65.45436767168943,81.40139891517664,63.60466569716928,86.269853312268,36.77844400147458,85.90159869649175,64.7301901428524,35.40304596537073,54.0220212410003,99.60877652683344,6.107564992824177,53.829100641282935,35.43303611106384,40.2777269802133,10.28119909408205,98.76364015651372,82.71403610397405,23.091279887612604,26.63695031040605,98.55231050146213,64.24041371621844,49.80999549552768,17.319735163007465,94.52593398495186,40.43283085300783,32.56065442918236,80.83982533114505,43.30871264880706,60.853499522069676,2.3742781610175956,32.19239790835231,2.6972984080312234,28.830622844756924,91.2822430056811,13.015213522137381,63.02216734543381,32.667492129915,81.69722944914804,53.999235124910996,42.850339665555815,0.5985065993678873,69.55186455865352,57.71289765284903,45.333854255385475,66.72262015801786,77.42635644067882,58.80439455147643,24.902309041362624,58.249573695884024,85.90707349183171]
## left panel
ax1.scatter(x,y,color='blue',s=5,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square


## right panel
ax2 = fig.add_subplot(122)
props = dict(alpha=0.5, edgecolors='none' )

handles = []
colors = ['blue', 'green', 'magenta', 'cyan']
for color in colors:
    x = np.random.randn(N)
    y = np.random.randn(N)
    s = np.random.randint(50,200)
    handles.append(ax2.scatter(x, y, c=color, s=s, **props))

ax2.set_ylim([-5,11])
ax2.set_xlim([-5,11])

ax2.legend(handles, colors)
ax2.grid(True)
ax2.set_aspect(1./ax2.get_data_ratio())
plt.show()