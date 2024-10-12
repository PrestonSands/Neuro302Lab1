#figure 1D
fig = plt.figure(figsize=(11.32, 5.5), dpi=150)
gs1d = gridspec.GridSpec(2, 2, hspace=-0.02, wspace=0.1)

time1 = 1032000
time2 = 1072000

time3 = 1062000
time4 = 1066800

#plot1
ax1 = fig.add_subplot(gs1d[0, 0])
plt.plot(spine2trials['block_23'][0,time1:time2],
        color = 'black',
        linewidth = 0.2
        )
ax1.set_xticks([0, 4000, 40000])
ax1.set_yticks([-0.035, 0, 0.01, 0.025])

ax1.set_xbound([0, 40000])
ax1.set_ybound([-0.035, 0.025])

#plot2
ax2 = fig.add_subplot(gs1d[0, 1])
plt.plot(spine2trials['block_23'][0,time3:time4],
        color = 'black',
        linewidth = 0.4
        )
ax2.set_xticks([0, 400, 4800])
ax2.set_yticks([-0.035, 0, 0.01, 0.025])

ax2.set_xbound([0, 4800])
ax2.set_ybound([-0.035, 0.025])

#plot3
ax3 = fig.add_subplot(gs1d[1, 0])
plt.plot(spine2trials['block_23'][1,time1:time2],
        color = 'black',
        linewidth = 0.8
        )
ax3.set_xticks([0, 4000, 40000])
ax3.set_yticks([-0.2, 0, 0.1, 0.2])

ax3.set_xbound([0, 40000])
ax3.set_ybound([-0.4, 0.4])

#plot4
ax4 = fig.add_subplot(gs1d[1, 1])
plt.plot(spine2trials['block_23'][1,time3:time4],
        color = 'black',
        linewidth = 0.8
        )
ax4.set_xticks([0, 400, 4800])
ax4.set_yticks([-0.2, 0, 0.1, 0.2])

ax4.set_xbound([0, 4800])
ax4.set_ybound([-0.4, 0.4])

#clean
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
ax4.axis('off')

plt.tight_layout()
plt.show()
