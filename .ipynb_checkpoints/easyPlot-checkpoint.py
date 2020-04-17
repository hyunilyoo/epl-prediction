

def e_barplot(df1, df2, lists, **kwargs):
    """
    Optional parameters:
    
    w: width of plot, h: height of plot, figname: name of image when you save a plot as an image,
    save: whether to save a plot as an image, t_fsize: title font size, l_fsize: legend font size,
    label_size: X and Y axis font size, n_labels: name of labels, title: plot title, interval: interval of X tick.
    """
    plot_features = {}
    for key, value in kwargs.items():
        plot_features[key] = value
    # Set default values   
    if 'w' not in plot_features:
        plot_features['w'] = 10
    if 'h' not in plot_features:
        plot_features['h'] = 10
    if 'figname' not in plot_features:
        plot_features['figname'] = 'h_barplot'
    if 'save' not in plot_features:
        plot_features['save'] = False
    if 't_fsize' not in plot_features:
        plot_features['t_fsize'] = 20
    if 'l_fsize' not in plot_features:
        plot_features['l_fsize'] = 10
    if 'label_size' not in plot_features:
        plot_features['label_size'] = 20
    if 'n_labels' not in plot_features:
        plot_features['n_labels'] = ['First DF', 'Second DF']
    if 'title' not in plot_features:
        plot_features['title'] = None
    if 'interval' not in plot_features:
        plot_features['interval'] = 10
    if 'x_range' not in plot_features:
        plot_features['x_range'] = [0, 50]
    if 'vis_col' not in plot_features:
        plot_features['vis_col'] = 1
    if 'vis_row' not in plot_features:
        plot_features['vis_row'] = len(lists)
    if 'func' not in plot_features:
        plot_features['func'] = None
    
    if len(lists) == 1:
        plt.subplots(len(lists), 1, figsize = (plot_features['w'], plot_features['h']))
        plt.bar(df1[lists[0]].value_counts().sort_index().index, df1[lists[0]].value_counts().sort_index().values, 
                color='purple', label=plot_features['n_labels'][0])
        plt.bar(df2[lists[0]].value_counts().sort_index().index, df2[lists[0]].value_counts().sort_index().values, 
                color='navy', label=plot_features['n_labels'][1])
        plt.xticks(np.arange(plot_features['x_range'][0], plot_features['x_range'][1], plot_features['interval']))
        plt.legend(fontsize = plot_features['l_fsize']) 
        plt.title(plot_features['title'], fontsize=plot_features['t_fsize'])
        plt.tick_params(labelsize = plot_features['label_size'])
        plt.tight_layout()
        if plot_features['save'] == True:
            plt.savefig(plot_features['figname'] + '.jpg')
    
    elif plot_features['vis_col'] == 1:
        f, axes = plt.subplots(len(lists), 1, figsize = (plot_features['w'], plot_features['h']))
        
        for i in range(len(lists)):
            axes[i].bar(df1[lists[i]].value_counts().sort_index().index, 
                        df1[lists[i]].value_counts().sort_index().values, 
                        color='purple', label=plot_features['n_labels'][0])
            axes[i].bar(df2[lists[i]].value_counts().sort_index().index, 
                        df2[lists[i]].value_counts().sort_index().values, 
                        color='navy', label=plot_features['n_labels'][1])
            axes[i].legend(fontsize = plot_features['l_fsize'])
            axes[i].set_xticks(np.arange(plot_features['x_range'][0], plot_features['x_range'][1], 
                                         plot_features['interval']))
            axes[i].set_title(lists[i], fontsize = plot_features['t_fsize'])
            axes[i].tick_params(labelsize=plot_features['label_size'])
            plt.tight_layout()
            if plot_features['save'] == True:
                plt.savefig(plot_features['figname'] + '.jpg')
                
    elif plot_features['func'] == 'average' and plot_features['vis_col'] > 1:
        r = plot_features['vis_row']
        c = plot_features['vis_col']
        
        r_uniq = list(np.arange(r))
        r_uniq = [[el] for el in r_uniq]
        c_uniq = list(np.arange(c))
        
        r_idx = []
        c_idx = c_uniq * r
        
        for num in r_uniq:
            r_idx += num * c
        
        f, axes = plt.subplots(r, c, figsize = (plot_features['w'], plot_features['h']))
        
        for i in range(len(lists)):
            axes[r_idx[i], c_idx[i]].bar(0, np.average(df1[lists[i]]), 
                                         color='purple', label=plot_features['n_labels'][0])
            axes[r_idx[i], c_idx[i]].bar(1, np.average(df2[lists[i]]), 
                                         color='navy', label=plot_features['n_labels'][1])
            axes[r_idx[i], c_idx[i]].legend(loc='upper right', fontsize = plot_features['l_fsize'], 
                                            frameon=True, shadow=True)
            axes[r_idx[i], c_idx[i]].set_title(lists[i], fontsize = plot_features['t_fsize'])
            axes[r_idx[i], c_idx[i]].tick_params(labelsize=plot_features['label_size'])
            plt.tight_layout()
            if plot_features['save'] == True:
                plt.savefig(plot_features['figname'] + '.jpg')  
                
    else:
        r = plot_features['vis_row']
        c = plot_features['vis_col']
        
        r_uniq = list(np.arange(r))
        r_uniq = [[el] for el in r_uniq]
        c_uniq = list(np.arange(c))
        
        r_idx = []
        c_idx = c_uniq * r
        
        for num in r_uniq:
            r_idx += num * c
        
        f, axes = plt.subplots(r, c, figsize = (plot_features['w'], plot_features['h']))
        
        for i in range(len(lists)):
            axes[r_idx[i], c_idx[i]].bar(df1[lists[i]].value_counts().sort_index().index, 
                                         df1[lists[i]].value_counts().sort_index().values, 
                                         color='purple', label=plot_features['n_labels'][0])
            axes[r_idx[i], c_idx[i]].bar(df2[lists[i]].value_counts().sort_index().index, 
                                         df2[lists[i]].value_counts().sort_index().values, 
                                         color='navy', label=plot_features['n_labels'][1])
            axes[r_idx[i], c_idx[i]].legend(fontsize = plot_features['l_fsize']) 
            axes[r_idx[i], c_idx[i]].set_xticks(np.arange(plot_features['x_range'][0], plot_features['x_range'][1], 
                                         plot_features['interval']))
            axes[r_idx[i], c_idx[i]].set_title(lists[i], fontsize = plot_features['t_fsize'])
            axes[r_idx[i], c_idx[i]].tick_params(labelsize=plot_features['label_size'])
            plt.tight_layout()
            if plot_features['save'] == True:
                plt.savefig(plot_features['figname'] + '.jpg')
