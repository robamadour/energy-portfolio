import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def GetScenario(s,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T):
    data = pd.DataFrame({"Demand" : demand[:T,s],
                        "WindPower": y[0].value*windPF[:T,s],
                       "SolarPower": Cs*solarPF[:T,s],
                       "GasBase" : y[1].value,
                       "GasPeak": y[2].value*peakHour,
                       "GasOption": x[(s*T):((s+1)*T)].value,
                       "SpotMarket": x[(nScenarios*T+s*T):
                                         (nScenarios*T+(s+1)*T)].value,
                       "Time": pd.date_range('2021-01-01 00:00', '2021-01-01 23:45', freq = '15min')
                        })
    #data.Time = data.Time.dt.strftime('%H:%M')
    data = data.set_index('Time')
    return(data)

def GetAllVariables(x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T):
    data_s1 = GetScenario(0,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T)
    data_s2 = GetScenario(1,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T)
    data_s3 = GetScenario(2,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T)
    data_s4 = GetScenario(3,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T)
    data_s5 = GetScenario(4,x,y,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T)


    data_s1.columns = data_s1.columns + "_s1"
    data_s2.columns = data_s2.columns + "_s2"
    data_s3.columns = data_s3.columns + "_s3"
    data_s4.columns = data_s4.columns + "_s4"
    data_s5.columns = data_s5.columns + "_s5"


    data_all = pd.merge(data_s1,data_s2 ,left_index=True, right_index=True, how='inner')
    data_all = pd.merge(data_all,data_s3,left_index=True, right_index=True, how='inner')
    data_all = pd.merge(data_all,data_s4,left_index=True, right_index=True, how='inner')
    data_all = pd.merge(data_all,data_s5,left_index=True, right_index=True, how='inner')
    
    return(data_all)

def Plot1(xsol,ysol,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T,name):
    f, (ax1, ax2,ax3,ax4,ax5) = plt.subplots(5, 1, sharex=True)
    axs = [ax1, ax2,ax3,ax4,ax5]

    hours = mdates.HourLocator(interval = 2)
    h_fmt = mdates.DateFormatter('%H')
    width = 0.008
    px = 12
    py = 16

    #ax.stackplot(data.index,data.SolarPower,data.WindPower,data.GasBase,data.GasPeak,data.GasOption,
     #            data.SpotMarket)

    dataNames = ['SolarPower','WindPower','GasBase','GasPeak','GasOption',"SpotMarket"]
    Labels = ['Solar Power','Wind Power','Gas Base','Gas Peak','Gas Option',"Spot Market"]
    #Colors = ["tab:blue","tab:red","tab:orange","tab:green","tab:purple","tab:cyan"]
    Colors = plt.cm.Dark2(range(6))

    for s in range(5):
        data = GetScenario(s,xsol,ysol,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T) 
        tp = 0*data.iloc[:,0]
        tn = 0*data.iloc[:,0]
        for i in range(len(dataNames)):
            xd = data[dataNames[i]].copy()
            xp = xd.copy()
            xp[xd<0] = 0
            xn = xd.copy()
            xn[xd>0] = 0

            axs[s].bar(data.index,xp,width,color=Colors[i],bottom = tp,label=Labels[i])
            axs[s].bar(data.index,xn,width,color=Colors[i],bottom = tn,label='_nolegend_')

            tp += xp
            tn += xn

        axs[s].plot(data.index,data.Demand,color="k")
        axs[s].set_xlim([data.index[0],  data.index[len(data.index)-1]+ timedelta(minutes=15)])
        axs[s].set_ylim(-4,12)
        axs[s].set_title("Scenario "+str(s+1))

        if s==2:
            axs[s].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #handles, labels = axs[0].get_legend_handles_labels()
    #f.legend()
    f.set_size_inches(px,py)
    #Then tick and format with matplotlib:
    axs[0].xaxis.set_major_locator(hours)
    axs[0].xaxis.set_major_formatter(h_fmt)

    f.autofmt_xdate()
    plt.show()
    f.savefig(name+'.png',bbox_inches = 'tight')
    f.savefig(name+'.pdf',bbox_inches = 'tight')
