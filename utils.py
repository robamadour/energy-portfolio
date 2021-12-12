import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def PlotPowerFactors(windPF,solarPF,T):
    data = pd.DataFrame({"WindPower_s1":  windPF[:T,0],
                         "SolarPower_s1": solarPF[:T,0],
                         "WindPower_s2":  windPF[:T,1],
                         "SolarPower_s2": solarPF[:T,1],
                         "WindPower_s3":  windPF[:T,2],
                         "SolarPower_s3": solarPF[:T,2],
                         "WindPower_s4":  windPF[:T,3],
                         "SolarPower_s4": solarPF[:T,3],
                         "WindPower_s5":  windPF[:T,4],
                         "SolarPower_s5": solarPF[:T,4],                       
                         "Time": pd.date_range('2021-01-01 00:00', '2021-01-01 23:45', freq = '15min')
                        })
    
    data = data.set_index('Time')
    
    # Plot
    f, (ax1, ax2,ax3,ax4,ax5) = plt.subplots(5, 1, sharex=True)
    axs = [ax1, ax2,ax3,ax4,ax5]

    hours = mdates.HourLocator(interval = 2)
    h_fmt = mdates.DateFormatter('%H')
    width = 0.008
    px = 12
    py = 16

    #ax.stackplot(data.index,data.SolarPower,data.WindPower,data.GasBase,data.GasPeak,data.GasOption,
     #            data.SpotMarket)

    dataNames = ['WindPower','SolarPower']
    Labels = ['Wind Power','Solar Power']
    #Colors = ["tab:blue","tab:red","tab:orange","tab:green","tab:purple","tab:cyan"]
    Colors = plt.cm.Dark2(range(6))

    for s in range(5):
        dataNameS  = [dataNames[0]+"_s"+str(s+1),dataNames[1]+"_s"+str(s+1)]
        tp = 0*data.iloc[:,0]
        tn = 0*data.iloc[:,0]
        
        axs[s].plot(data.index,data[dataNameS[0]],color="b",label = Labels[0])
        axs[s].plot(data.index,data[dataNameS[1]],color="g",label = Labels[1])

        axs[s].set_xlim([data.index[0],  data.index[len(data.index)-1]+ timedelta(minutes=15)])
        axs[s].set_ylim(0,0.8)
        axs[s].set_title("Scenario "+str(s+1))
        axs[s].grid()

        if s==2:
            axs[s].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #handles, labels = axs[0].get_legend_handles_labels()
    #f.legend()
    f.set_size_inches(px,py)
    #Then tick and format with matplotlib:
    axs[0].xaxis.set_major_locator(hours)
    axs[0].xaxis.set_major_formatter(h_fmt)
    axs[0].set_xlabel("Time")
    
    f.autofmt_xdate()
    plt.show()
    name = "outputs/renewable_gen"
    f.savefig(name+'.png',bbox_inches = 'tight')
    f.savefig(name+'.pdf',bbox_inches = 'tight')
    
def PlotAllVars(windPF,solarPF,demand,rtPrice,T):
    data = pd.DataFrame({"WindPower_s1":  windPF[:T,0],
                         "SolarPower_s1": solarPF[:T,0],
                         "Demand_s1":  demand[:T,0],
                         "Price_s1": rtPrice[:T,0],
                         
                         "WindPower_s2":  windPF[:T,1],
                         "SolarPower_s2": solarPF[:T,1],
                         "Demand_s2":  demand[:T,1],
                         "Price_s2": rtPrice[:T,1],
                         
                         "WindPower_s3":  windPF[:T,2],
                         "SolarPower_s3": solarPF[:T,2],
                         "Demand_s3":  demand[:T,2],
                         "Price_s3": rtPrice[:T,2],
                         
                         "WindPower_s4":  windPF[:T,3],
                         "SolarPower_s4": solarPF[:T,3],
                         "Demand_s4":  demand[:T,3],
                         "Price_s4": rtPrice[:T,3],
                         
                         "WindPower_s5":  windPF[:T,4],
                         "SolarPower_s5": solarPF[:T,4],
                         "Demand_s5":  demand[:T,4],
                         "Price_s5": rtPrice[:T,4],
                         
                         "Time": pd.date_range('2021-01-01 00:00', '2021-01-01 23:45', freq = '15min')
                        })
    
    data = data.set_index('Time')
    
    # Plot
    f, axs = plt.subplots(5, 2, sharex=True)

    hours = mdates.HourLocator(interval = 2)
    h_fmt = mdates.DateFormatter('%H')
    width = 0.008
    px = 12
    py = 16

    #ax.stackplot(data.index,data.SolarPower,data.WindPower,data.GasBase,data.GasPeak,data.GasOption,
     #            data.SpotMarket)

    dataNames = ['WindPower','SolarPower',"Demand","Price"]
    Labels = ['Wind Power','Solar Power',"Demand","Price"]
    #Colors = ["tab:blue","tab:red","tab:orange","tab:green","tab:purple","tab:cyan"]
    Colors = plt.cm.Dark2(range(6))

    for s in range(5):
        dataNameS  = [dataNames[0]+"_s"+str(s+1),dataNames[1]+"_s"+str(s+1)]
        tp = 0*data.iloc[:,0]
        tn = 0*data.iloc[:,0]
        
        axs[s,0].plot(data.index,data[dataNameS[0]],color="b",label = Labels[0])
        axs[s,0].plot(data.index,data[dataNameS[1]],color="g",label = Labels[1])

        axs[s,0].set_xlim([data.index[0],  data.index[len(data.index)-1]+ timedelta(minutes=15)])
        axs[s,0].set_ylim(0,0.8)
        axs[s,0].set_ylabel('Power [p.f.]')
        axs[s,0].set_title("Wind and Solar Power Factor in Scenario "+str(s+1))
        axs[s,0].grid()

        if s==2:
            axs[s,0].legend(loc='center left', bbox_to_anchor=(2.3, 0.15))
    #handles, labels = axs[0].get_legend_handles_labels()
    #f.legend()
    f.set_size_inches(px,py)
    #Then tick and format with matplotlib:
    axs[0,0].xaxis.set_major_locator(hours)
    axs[0,0].xaxis.set_major_formatter(h_fmt)
    axs[4,0].xaxis.set_label_text("Time")
    
    for s in range(5):
        dataNameS  = [dataNames[2]+"_s"+str(s+1),dataNames[3]+"_s"+str(s+1)]
        tp = 0*data.iloc[:,0]
        tn = 0*data.iloc[:,0]
        
        axs[s,1].plot(data.index,data[dataNameS[0]],color="m",label = Labels[2])
        ax2 = axs[s,1].twinx()
        ax2.plot(data.index,data[dataNameS[1]],color="c",label = Labels[3])

        axs[s,1].set_xlim([data.index[0],  data.index[len(data.index)-1]+ timedelta(minutes=15)])
        axs[s,1].set_ylim(6,12)
        axs[s,1].set_ylabel('Demand [Mw]')
        ax2.set_ylim(0,32)
        ax2.set_ylabel('Price [$/Mwh]')
        axs[s,1].set_title("Demand and Price in Scenario "+str(s+1))
        
        axs[s,1].grid()

        if s==(2):
            axs[s,1].legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
            ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.35))
    #handles, labels = axs[0].get_legend_handles_labels()
    #f.legend()
    f.set_size_inches(px,py)
    #Then tick and format with matplotlib:
    axs[0,1].xaxis.set_major_locator(hours)
    axs[0,1].xaxis.set_major_formatter(h_fmt)
    axs[4,1].xaxis.set_label_text("Time")
    
    f.autofmt_xdate()
    plt.show()
    name = "outputs/renewable_gen_demand"
    f.savefig(name+'.png',bbox_inches = 'tight')
    f.savefig(name+'.pdf',bbox_inches = 'tight')


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

def PlotEnergyMix(xsol,ysol,demand,windPF,solarPF,Cs,nScenarios,peakHour,rtPrice,T,name):
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
        axs[s].set_ylabel('Power [Mw]')
        axs[s].set_title("Scenario "+str(s+1))
        axs[s].grid()

        if s==2:
            axs[s].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #handles, labels = axs[0].get_legend_handles_labels()
    #f.legend()
    f.set_size_inches(px,py)
    #Then tick and format with matplotlib:
    axs[0].xaxis.set_major_locator(hours)
    axs[0].xaxis.set_major_formatter(h_fmt)
    axs[4].xaxis.set_label_text("Time")

    f.autofmt_xdate()
    plt.show()
    f.savefig(name+'.png',bbox_inches = 'tight')
    f.savefig(name+'.pdf',bbox_inches = 'tight')
