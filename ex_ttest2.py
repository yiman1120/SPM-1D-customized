import numpy as np
import matplotlib.pyplot as plt
import spm1d


"""
# load plain-text data (30 rows, 100 columns):
# dir0         = os.path.dirname(__file__)
#fname        = 'C:\\Users\\User\\Downloads\\spm1d-master\\spm1d-master\\spm1d\\examples\\io\\data\\ex_kinematics.txt'
fname        = 'C:\\Users\\User\\anaconda3\\Lib\\site-packages\\spm1d\\data\\datafiles\\OUKA_XR_F.txt'
Y            = np.loadtxt(fname)   #30 curves, 100 nodes

# plot:
plt.close('all')
plt.plot(Y.T, color = 'k')
plt.xlabel('Time (%)', size=20)
plt.ylabel(r'$\theta$ (deg)', size=20)
plt.show()
"""


#(0) Load data:
dataset      = spm1d.data.uv1d.t2.PlantarArchAngle()
# dataset      = spm1d.data.uv1d.t2.SimulatedTwoLocalMax()
YA,YB        = dataset.get_data()
print( dataset )


#(1) Conduct t test:
alpha      = 0.05
t          = spm1d.stats.ttest2(YB, YA, equal_var=False)
ti         = t.inference(alpha, two_tailed=True, interp=True)
print( ti )



#(2) Plot:
plt.close('all')
### plot mean and SD:
fig,AX = plt.subplots( 1, 2, figsize=(8, 3.5) )
ax     = AX[0]
plt.sca(ax)
spm1d.plot.plot_mean_sd(YA, linecolor='b', facecolor=(0.7,0.7,1), edgecolor='b', label='OUKA')
spm1d.plot.plot_mean_sd(YB, linecolor='r', facecolor=(1,0.7,0.7), edgecolor='r', label='XR TKA')
ax.axhline(y=0, color='k', linestyle=':')
ax.set_xlabel('Time (%)')
ax.set_ylabel('Knee Flexion-Extension (deg)')
#ax.set_ylabel('Knee Varus-Valgus (deg)')
#ax.set_ylabel('Knee Rotation (deg)')
ti.plot_p_values(size=10, offset_all_clusters=(0,0.9))
plt.legend(loc='upper left')

# Shade regions where p-values < 0.05
if ti.h0reject:
    for cluster in ti.clusters:
        if cluster.p < alpha:
            start, end = cluster.endpoints
            ax.axvspan(start, end, color='gray', alpha=0.3)

### plot SPM results:
ax     = AX[1]
plt.sca(ax)
ti.plot()
ti.plot_threshold_label(fontsize=8)
ti.plot_p_values(size=10, offset_all_clusters=(0,0.9))
ax.set_xlabel('Time (%)')
plt.tight_layout()
plt.show()
