#run each of these in a different block of code, can take up to 3 mins to run each

#spontaneous spike sorting
sortedSpontaneous = ntk.sort_spikes(spontaneousConcat[0], fs=dataset.fs)
sortedSpontaneous.hand_pick_clusters()

sortedSpontaneous.plot_clusters()
sortedSpontaneous.plot_pca() 

#spine 1 sorting
sortedSpine1 = ntk.sort_spikes(spine1concat[0], fs=dataset.fs)
sortedSpine1.hand_pick_clusters()

sortedSpine1.plot_clusters()
sortedSpine1.plot_pca() 

#spine 2 sorting
sortedSpine2 = ntk.sort_spikes(spine2concat[0], fs=dataset.fs)
sortedSpine2.hand_pick_clusters()

sortedSpine2.plot_clusters()
sortedSpine2.plot_pca() 

#spine 3 sorting
sortedSpine3 = ntk.sort_spikes(spine3concat[0], fs=dataset.fs)
sortedSpine3.hand_pick_clusters()

sortedSpine3.plot_clusters()
sortedSpine3.plot_pca() 

#spine 4 sorting
sortedSpine4 = ntk.sort_spikes(spine4concat[0], fs=dataset.fs)
sortedSpine4.hand_pick_clusters()

sortedSpine4.plot_clusters()
sortedSpine4.plot_pca() 

#wave displayer
cluster_waveforms = sortedSpine4.get_cluster_waveforms(2)
print(cluster_waveforms.shape)
plt.plot(cluster_waveforms[0])
plt.show()

#PCA cluster compare
group_1_transformed, group_2_transformed = compare_clusters(sortedSpontaneous, sortedSpine1, 'sortedSpontaneous', 'sortedSpine1')
group_1_transformed, group_2_transformed = compare_clusters(sortedSpontaneous, sortedSpine1, 'sortedSpontaneous', 'sortedSpine2')
group_1_transformed, group_2_transformed = compare_clusters(sortedSpontaneous, sortedSpine1, 'sortedSpontaneous', 'sortedSpine3')
group_1_transformed, group_2_transformed = compare_clusters(sortedSpontaneous, sortedSpine1, 'sortedSpontaneous', 'sortedSpine4')
